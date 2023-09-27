from rest_framework.serializers import ModelSerializer

from comments.models import Post, Commentary


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_at']


class CommentarySerializer(ModelSerializer):
    class Meta:
        model = Commentary
        fields = ['binding', 'binding_com', 'captcha', 'text', 'binding', 'binding_com']



