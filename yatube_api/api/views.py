from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post_id'))
