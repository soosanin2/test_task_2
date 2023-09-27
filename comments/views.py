from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework.viewsets import ModelViewSet

from .models import Post, Commentary, CustomUser
from .forms import PostForm, RegistrationForm, CommentaryForm
from collections import defaultdict

from .serializers import PostSerializer, CommentarySerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def post_app(request):
    return render(request, 'comments/post_app.html')


class CommentaryView(ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


def home(request):
    data = {
        'avatar': CustomUser.objects.all(),
        'post': Post.objects.order_by('-created_at'),
        'commentary': Commentary.objects.order_by('-created_at'),
        'fdata': submit_comment(request),

    }
    print(data)

    return render(request, 'comments/home.html', {'data': data})


def task(request):
    return render(request, 'comments/task.html')


def create_post(request):
    error = ''

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
        else:
            error = 'Введены не коректные данные'

    form = PostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'comments/create_post.html', data)


def registration(request):
    error = ''

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error = 'Введите коректные данные'

    form = RegistrationForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'comments/registration.html', data)


def submit_comment(request):
    error = ''

    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('home')
        else:
            error = 'Введены не коректные данные'
    else:
        pass

    form = CommentaryForm()
    form_data = {
        'form': form,
        'error': error,
    }
    print(f"fdata{form_data}")
    return form_data
