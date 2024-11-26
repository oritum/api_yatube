"""Кастомные permissions для api_yatube."""

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.exceptions import PermissionDenied


class IsAuthentificatedAndAuthorPermission(BasePermission):
    """
    Проверка прав пользвателей на просмотр, создание и
    редактирование объектов:
    - для неаутентифицированных пользователей доступ закрыт;
    - аутентифицированные пользователи могут просматривать все объекты,
    создавать новые и редактировать/удалять только свои.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.author != request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        return True
