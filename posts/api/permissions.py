# for custom permissions:

from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'You are not authorized user to view this post'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user