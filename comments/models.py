import os
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from captcha.fields import CaptchaField
from django.contrib.auth import get_user_model


def user_file_path(instance, filename):
    user_id_name = str(instance.author.id) + str(instance.author.username)

    if filename.endswith(('.jpg', '.png', '.gif')):
        upload_to = 'uploads/img/'
    elif filename.endswith('.txt'):
        upload_to = 'uploads/text/'
    else:
        return None  # Неизвестный формат файла

    post_id = str(instance.title)

    return f'{upload_to}{user_id_name}/{post_id}/{filename}'



class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/No_image.png')
    home_page = models.URLField(max_length=255, blank=True, null=True, verbose_name="Home Page", )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return 'media/avatars/No_image.png'




class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author_article", blank=True,
                               null=True, )
    your_file = models.FileField(
        upload_to=user_file_path, blank=True, null=True, verbose_name="Your File",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif', 'txt']),
                    ])
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.author, self.title)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if self.your_file:
            # Если загружено изображение, обработать его
            if self.your_file.name.endswith(('.jpg', '.png', '.gif')):
                max_width = 320
                max_height = 240
                image = Image.open(self.your_file)
                width, height = image.size

                # Проверить размер изображения и изменить его, если необходимо
                if width > max_width or height > max_height:
                    image.thumbnail((max_width, max_height),  Image.BOX)
                    image.save(self.your_file.path)

            # Если загружен текстовый файл, проверить его размер
            elif self.your_file.name.endswith('.txt'):
                max_size_kb = 100
                file_size = self.your_file.size  # Размер файла в байтах

                if file_size > max_size_kb * 1024:  # Перевести в килобайты
                    raise ValidationError(f"Максимальный размер текстового файла - {max_size_kb} KB.")

        super().save(*args, **kwargs)



class Commentary(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True,
                                related_name='comments_articles')
    binding_com = models.IntegerField(verbose_name="Binding_com", blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author_article", blank=True, null=True)

    captcha = CaptchaField()
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"



