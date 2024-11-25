from posts.models import Comment, Group, Post
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    post = ReadOnlyField(source='post_id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
