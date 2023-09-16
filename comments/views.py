from django.shortcuts import render

from .models import Post, Review, User


def home(request):
    return render(request, 'base.html')


def news_post(request):
    data = {
    'post': Post.objects.order_by('title'),
    'review': Review.objects.order_by('user_name'),
    }
    return render(request, 'comments/comments.html', {'data': data})


def comm_page(request):
    data = {
        'comm_title': 'Lorem ipsum',
        'comm_text': 'Lorem ipsum dolor sit amet.'
    }
    return render(request, 'comments/comments.html', data)

