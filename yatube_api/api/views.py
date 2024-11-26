from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.serializers import Serializer
from typing import Any, Type, Union


class AuthorPermissionMixin:
    """
    Миксин для проверки прав автора на создание, изменение и удаление
    объектов.
    """

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(author=self.request.user)

    def perform_update(self, serializer: Serializer) -> None:
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance: Union[Comment, Post]) -> None:
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)


class PostViewSet(AuthorPermissionMixin, ModelViewSet):
    """ViewSet для управления постами. Включает проверку прав автора."""

    queryset = Post.objects.all()
    serializer_class: Type[PostSerializer] = PostSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    """ViewSet для просмотра групп. Только для чтения."""

    queryset = Group.objects.all()
    serializer_class: Type[GroupSerializer] = GroupSerializer


class CommentViewSet(AuthorPermissionMixin, ModelViewSet):
    """ViewSet для управления комментариями. Включает проверку прав автора."""

    serializer_class: Type[CommentSerializer] = CommentSerializer

    def get_queryset(self) -> Any:
        return Comment.objects.filter(post=self.kwargs.get('post_id'))

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get('post_id')),
        )
