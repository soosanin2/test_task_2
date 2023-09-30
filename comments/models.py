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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author_article", blank=True, null=True, )

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.author, self.title)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Commentary(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True,
                                related_name='comments_articles')
    binding_com = models.IntegerField(verbose_name="Binding_com", blank=True, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author_article", blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author_article", blank=True, null=True)
    your_file = models.FileField(upload_to=user_file_path, blank=True, null=True, verbose_name="Your File")
    captcha = models.CharField(max_length=255, verbose_name="Captcha")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentarys"

