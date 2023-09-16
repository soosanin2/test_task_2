from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comments', views.news_post, name='news_post'),
    path('comments', views.comm_page, name='comments'),

]


