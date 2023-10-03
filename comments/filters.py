import django_filters
from .models import Commentary

class CommentaryFilter(django_filters.FilterSet):
    class Meta:
        model = Commentary
        fields = {
            'author__username': ['exact', 'icontains'],
            'created_at': ['exact', 'gte', 'lte'],
            # Добавьте другие поля, по которым вы хотите фильтровать
        }