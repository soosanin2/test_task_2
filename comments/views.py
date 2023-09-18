from django.shortcuts import render

from .models import Post, Review, CustomUser


def home(request):
    return render(request, 'home.html')


def news_post(request):
    data = {
    'avatar': CustomUser.objects.order_by('username'),
    'post': Post.objects.order_by('title'),
    'review': Review.objects.order_by('user__username'),
    }
    print(data)
    return render(request, 'comments/comments.html', {'data': data})



def comm_page(request):
    data = {
        'comm_title': 'Lorem ipsum',
        'comm_text': 'Lorem ipsum dolor sit amet.'
    }
    return render(request, 'comments/comments.html', data)

