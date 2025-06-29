from rest_framework import permissions
from core.apps.accounts.choices.user import RoleChoice


class IsParent(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        if request.user.role != RoleChoice.PARENT.value:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
