from posts.models import Comment, Group, Post
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
