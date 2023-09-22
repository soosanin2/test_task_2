
from django.contrib.auth.forms import UserCreationForm
from .models import Post, CustomUser, Commentary
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, ImageField, forms


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['captcha', 'text', 'binding', 'binding_com']

        widgets = {
            'binding': TextInput(attrs={
                'class': 'binding',
            }),
            'binding_com': TextInput(attrs={
                'class': 'binding',
            }),
            'captcha': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Капча"
            }),
            'text':  TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Коментарий"
            }),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заголовок"
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи"
            }),
        }


class RegistrationForm(UserCreationForm):
    # model = forms.EmailField(max_length=254, help_text='Обов\'язкове поле. Введіть правильну email адресу.')
    avatar = ImageField(required=False)  # Додайте поле для аватарки з параметром required=False

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'avatar' )

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя"
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "email"
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Придумайте пароль"
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Повторите пароль"
            }),
        }

