from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, CustomUser, Commentary
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, ImageField


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary

        fields = ('binding_com', 'captcha', 'text', 'your_file',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

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
