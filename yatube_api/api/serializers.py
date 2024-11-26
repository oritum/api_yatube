from posts.models import Comment, Group, Post
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class PostSerializer(ModelSerializer):
    """Сериализатор для модели Post."""
    author: ReadOnlyField = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(ModelSerializer):
    """Сериализатор для модели Comment."""
    author: ReadOnlyField = ReadOnlyField(source='author.username')
    post: ReadOnlyField = ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
