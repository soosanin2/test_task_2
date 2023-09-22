from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('create_post', views.create_post, name="create_post"),
    path('registration', views.registration, name="registration"),
    path('submit_comment', views.submit_comment, name='submit_comment'),

]


