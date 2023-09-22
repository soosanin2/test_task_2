import os
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


def user_file_path(instance, filename):
    user_id_name = str(instance.user.id)+str(instance.user.username)
    if filename.endswith(('.jpg', '.png', '.gif')):
        return f'uploads/img/{user_id_name}/{filename}'
    elif filename.endswith(('.txt')):
        return f'uploads/text/{user_id_name}/{filename}'
    else:
        pass

# def binding_com(instanse):
#     binding = int(instanse.post.id)
#     return



class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    home_page = models.URLField(max_length=255, blank=True, null=True, verbose_name="Home Page", )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return 'media/avatars/No_image.png'


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Commentary(models.Model):
    binding = models.IntegerField(verbose_name="Binding")
    binding_com = models.IntegerField(verbose_name="Binding_com", blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    your_file = models.FileField(upload_to=user_file_path, blank=True, null=True, verbose_name="Your File")
    captcha = models.CharField(max_length=255, verbose_name="Captcha")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentarys"





