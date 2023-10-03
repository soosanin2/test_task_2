from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, CustomUser, Commentary
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, ImageField
from captcha.fields import CaptchaField



class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CommentaryForm(ModelForm):

    class Meta:
        model = Commentary

        fields = ('binding_com', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'




class CommentaryWithCaptchaForm(CommentaryForm):
    captcha = CaptchaField()


class RegisterUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'avatar', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user




class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ('title', 'your_file', 'text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'text', 'your_file',]
#
#         widgets = {
#             "title": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': "Заголовок"
#             }),
#             "text": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': "Текст статьи"
#             }),
#         }
