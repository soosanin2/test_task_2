from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import PostView, CommentaryView, commentary_app, RecCommView

router = SimpleRouter()

router.register('api/post', PostView)
router.register('api/commentary', CommentaryView)
router.register('api/reccromm', RecCommView)
# http://127.0.0.1:8000/api/commentary/?format=json


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeListView.as_view(), name='home'),
    path('login', views.ProjectLoginView.as_view(), name='login_page'),
    path('logout', views.ProjectLogoutView.as_view(), name='logout_page'),
    path('detail/<int:pk>', views.DetailListView.as_view(), name='detail_page'),
    path('task', views.task, name='task'),
    path('edit-page', views.PostCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.PostUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.PostDeleteView.as_view(), name='delete_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    # path('create_post', views.create_post, name="create_post"),
    # path('registration', views.registration, name="registration"),
    # path('submit_comment/', views.submit_comment, name='submit_comment'),
    # path('post_app', post_app, name='post_app'),
    path('commentary_app', commentary_app, name='commentary_app'),


]

urlpatterns += router.urls
