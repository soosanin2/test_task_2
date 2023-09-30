from rest_framework.fields import ReadOnlyField, DateTimeField, ListField
from rest_framework.serializers import ModelSerializer

from comments.models import Post, Commentary


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['author_username', 'title', 'text', 'created_at']


class CommentarySerializer(ModelSerializer):

    author_username = ReadOnlyField(source='user.username')
    created_at = DateTimeField(format="%d.%m.%Y в %H:%M", read_only=True)
    id_list = ReadOnlyField(source='commentary.id')

    class Meta:
        model = Commentary
        fields = ['article', 'binding_com', 'author_username', 'captcha', 'text', 'created_at', 'id', 'id_list']


class RecCommSerializer(ModelSerializer):

    bind_list = ListField()
    bind_com_list = ListField()

    class Meta:
        model = Commentary
        fields = ['binding', 'binding_com', 'id', 'bind_list', 'bind_com_list']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        unique_bindings = Commentary.objects.values_list('binding', flat=True).distinct()
        unique_bindings_com = Commentary.objects.values_list('binding_com', flat=True).distinct()

        self.fields['bind_list'].default = list(unique_bindings)
        self.fields['bind_com_list'].default = list(unique_bindings_com)