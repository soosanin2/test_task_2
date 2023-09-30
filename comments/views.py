from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import ModelViewSet

from .models import Post, Commentary, CustomUser
from .forms import PostForm, CommentaryForm, AuthUserForm, RegisterUserForm
from collections import defaultdict

from .serializers import PostSerializer, CommentarySerializer, RecCommSerializer


class HomeListView(ListView):
    model = Post
    template_name = 'comments/home.html'
    context_object_name = "list_articles"


class ProjectLoginView(LoginView):
    template_name = 'comments/login_page.html'
    form_class = AuthUserForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


class ProjectLogoutView(LogoutView):
    next_page = reverse_lazy("home")


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
        self.object.author
        self.request.uzer

        if self.request.user != self.object.author:
            return HttpResponseForbidden("У вас нет разрешения на удаление этой статьи.")

        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class DetailListView(FormMixin, DetailView):
    model = Post
    template_name = 'comments/detail_page.html'
    context_object_name = "get_article"


    form_class = CommentaryForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_page', kwargs={'pk': self.object.article.id})


class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'comments/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


# def post_app(request):
#     return render(request, 'comments/home.html')


class CommentaryView(ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


def commentary_app(request):
    return render(request, 'comments/home.html')


class RecCommView(ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = RecCommSerializer


def rec_comm_app(request):
    return render(request, 'comments/home.html')



def task(request):
    return render(request, 'comments/task.html')

#
# def create_post(request):
#     error = ''
#
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.author = request.user
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Введены не коректные данные'
#
#     form = PostForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'comments/create_post.html', data)

#
# def registration(request):
#     error = ''
#
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             error = 'Введите коректные данные'
#
#     form = RegistrationForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'comments/registration.html', data)

#
# def submit_comment(request):
#
#     error = ''
#
#     if request.method == 'POST':
#         form = CommentaryForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.save()
#             return redirect('home')
#         else:
#             error = 'Введены не коректные данные'
#     else:
#         pass
#
#     form = CommentaryForm()
#     form_data = {
#         'form': form,
#         'error': error,
#     }
#     return form_data

