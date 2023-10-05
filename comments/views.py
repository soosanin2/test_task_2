
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import clean_html


from .models import Post, Commentary, CustomUser
from .forms import PostForm, CommentaryForm, AuthUserForm, RegisterUserForm, CommentaryWithCaptchaForm

from .serializers import PostSerializer


def task(request):
    return render(request, 'comments/task.html')


class HomeListView(ListView):
    model = Post
    template_name = 'comments/home.html'
    context_object_name = "list_articles"
    ordering = ['-created_at']


class ProjectLoginView(LoginView):
    template_name = 'comments/login_page.html'
    form_class = AuthUserForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


class ProjectLogoutView(LogoutView):
    next_page = reverse_lazy("home")

# Попытка вывода через API
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login_page")
    model = Post
    template_name = 'comments/edit_page.html'
    form_class = PostForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Post.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login_page")
    model = Post
    template_name = 'comments/edit_page.html'
    form_class = PostForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        return kwargs


class PostDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = reverse_lazy("login_page")
    model = Post
    template_name = 'comments/edit_page.html'
    success_url = reverse_lazy("edit_page")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user != self.object.author:
            return HttpResponseForbidden("У вас нет разрешения на удаление этой статьи.")

        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class DetailListView(FormMixin, DetailView):
    model = Post
    template_name = 'comments/detail_page.html'
    context_object_name = "get_article"
    form_class = CommentaryWithCaptchaForm

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.article = self.get_object()
    #     self.object.author = self.request.user
    #     self.object.save()
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user

        # Очистите HTML-код, перед сохранением его в базу данных
        self.object.text = clean_html(self.object.text)

        self.object.save()
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_page', kwargs={'pk': self.object.article.id})

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sort_order = self.request.GET.get('sort_order', 'newest')

        comments = []
        if hasattr(self, 'object'):
            if sort_order == 'oldest':
                comments = self.object.comments_articles.all().order_by('created_at')

            elif sort_order == 'newest':
                comments = self.object.comments_articles.all().order_by('-created_at')

            elif sort_order == 'authorA':
                comments = self.object.comments_articles.all().order_by('-author__username')

            elif sort_order == 'authorZ':
                comments = self.object.comments_articles.all().order_by('author__username')

            elif sort_order == 'emailA':
                comments = self.object.comments_articles.all().order_by('author__email')

            elif sort_order == 'emailZ':
                comments = self.object.comments_articles.all().order_by('-author__email')

            page = self.request.GET.get('page')
            paginator = Paginator(comments, 25)

            try:
                comments = paginator.page(page)
            except PageNotAnInteger:
                comments = paginator.page(1)

            except EmptyPage:
                comments = paginator.page(paginator.num_pages)

        context['comments'] = comments
        context['sort_order'] = sort_order

        return context


    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         # Проверка CAPTCHA
    #         if not form.cleaned_data['captcha'].is_valid:
    #             return self.form_invalid(form)
    #
    #         self.object = form.save(commit=False)
    #         self.object.article = self.get_object()
    #         self.object.author = self.request.user
    #         self.object.save()
    #
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         # Проверка CAPTCHA
    #         if not form.cleaned_data['captcha'][0].is_valid:
    #
    #             return self.form_invalid(form)
    #
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = self.object.comments_articles.all().order_by('-created_at')
    #     return context



class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'comments/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        avatar = form.cleaned_data["avatar"]
        email = form.cleaned_data.get("email")
        aut_user = authenticate(username=username, password=password, avatar=avatar, email=email)
        login(self.request, aut_user)
        return form_valid


# def commentary_app(request):
#     return render(request, 'comments/home.html')


# def rec_comm_app(request):
#     return render(request, 'comments/home.html')





