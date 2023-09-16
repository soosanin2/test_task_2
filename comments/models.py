from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Поле для зв'язку з користувачем
    user_name = models.CharField(max_length=255, verbose_name="User Name")
    email = models.EmailField(max_length=100)
    home_page = models.URLField(blank=True, null=True, verbose_name="Home Page",
                                default='static/commands/img/user-astronaut-solid.svg')
    your_file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Your File")
    captcha = models.CharField(max_length=255, verbose_name="Captcha")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

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