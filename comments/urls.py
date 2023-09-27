from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import PostView, CommentaryView, post_app

router = SimpleRouter()

router.register('api/post', PostView)
router.register('api/commentary', CommentaryView)

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('create_post', views.create_post, name="create_post"),
    path('registration', views.registration, name="registration"),
    path('submit_comment', views.submit_comment, name='submit_comment'),
    path('post_app', post_app, name='post_app'),

]

urlpatterns += router.urls
