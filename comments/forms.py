from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, CustomUser, Commentary
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, ImageField
from captcha.fields import CaptchaField


# Форма аутентификации пользователей при входе в систему
class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #  Для каждого поля устанавливается атрибут CSS класса "form-control", чтобы изменить стиль на требуемый
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

# Форма создания комментариев
class CommentaryForm(ModelForm):

    class Meta:
        model = Commentary

        fields = ('binding_com', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



# Форма наследуется от CommentaryForm и добавляет CAPTCHA
class CommentaryWithCaptchaForm(CommentaryForm):
    captcha = CaptchaField()

# Форма регистрации новых пользователей
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



# Форма создания и редактирования статей
class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ('title', 'your_file', 'text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



# для API
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
