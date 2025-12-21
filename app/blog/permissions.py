from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrModeratorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            if request.user.groups.filter(name='Moderator').exists():
                return True

        return False
