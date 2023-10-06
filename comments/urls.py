from django.urls import path
# from rest_framework.routers import SimpleRouter

from . import views

# для API
# from .views import PostView

# router = SimpleRouter()
# router.register('api/post', PostView)
# http://127.0.0.1:8000/api/post/?format=json


urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('login', views.ProjectLoginView.as_view(), name='login_page'),
    path('logout', views.ProjectLogoutView.as_view(), name='logout_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('detail/<int:pk>', views.DetailListView.as_view(), name='detail_page'),
    path('task', views.task, name='task'),
    path('edit-page', views.PostCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.PostUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.PostDeleteView.as_view(), name='delete_page'),

]

# для API
# urlpatterns += router.urls
