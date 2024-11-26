from rest_framework.serializers import ModelSerializer, SlugRelatedField

from posts.models import Comment, Group, Post


class AuthorBaseSerializer(ModelSerializer):
    """Базовый сериализатор для моделей Post и Comment."""

    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        abstract = True


class PostSerializer(AuthorBaseSerializer):
    """Сериализатор для модели Post."""

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(AuthorBaseSerializer):
    """Сериализатор для модели Comment."""

    post = SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
