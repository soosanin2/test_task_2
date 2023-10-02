from rest_framework.fields import ReadOnlyField, DateTimeField, ListField
from rest_framework.serializers import ModelSerializer

from comments.models import Post, Commentary


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['author_username', 'title', 'text', 'created_at']

