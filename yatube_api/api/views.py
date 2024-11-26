from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.permissions import IsAuthentificatedAndAuthorPermission
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class PermissionMixin(ModelViewSet):
    """
    Миксин для проверки прав пользвателей на просмотр, создание и
    редактирование объектов:
    - для неаутентифицированных пользователей доступ закрыт;
    - аутентифицированные пользователи могут просматривать все объекты,
    создавать новые и редактировать/удалять только свои.
    """

    permission_classes = [IsAuthentificatedAndAuthorPermission]


class PostViewSet(PermissionMixin):
    """ViewSet для управления постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """ViewSet для просмотра групп. Только для чтения."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionMixin):
    """ViewSet для управления комментариями."""

    serializer_class = CommentSerializer

    def get_post_id(self) -> int:
        return self.kwargs.get('post_id')

    def get_queryset(self) -> Any:
        return Comment.objects.filter(post=self.get_post_id())

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.get_post_id()),
        )
