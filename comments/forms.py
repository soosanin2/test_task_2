from .models import Post
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

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

