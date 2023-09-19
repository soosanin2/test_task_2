from django.shortcuts import render, redirect
from .models import Post, Commentary, CustomUser
from .forms import PostForm

def home(request):
    data = {
    # 'avatar': CustomUser.objects.order_by('username'),
    'avatar': CustomUser.objects.all(),
    # 'post': Post.objects.order_by('title'),
    'post': Post.objects.order_by('-created_at'),
    # 'commentary': Commentary.objects.order_by('user__username'),
        # User Name, E-mail, -created_at (как в порядке убывания, так и в обратном)
    'commentary': Commentary.objects.order_by('-created_at'),
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

