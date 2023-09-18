import os
from PIL import Image
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


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return 'media/avatars/No_image.png'



class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Поле для зв'язку з користувачем
    user_name = models.CharField(max_length=255, verbose_name="User Name", blank=True)
    email = models.EmailField(max_length=100, blank=True)
    home_page = models.URLField(max_length=255, blank=True, null=True, verbose_name="Home Page",)
    your_file = models.FileField(upload_to=user_file_path, blank=True, null=True, verbose_name="Your File")
    captcha = models.CharField(max_length=255, verbose_name="Captcha")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        if not self.user_name:
            self.user_name = self.user.first_name + " " + self.user.last_name
        if not self.email:
            self.email = self.user.email

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"



class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


