from rest_framework import permissions
from .models import Project
from django.db.models import Q


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return obj.author == request.user


class HasContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs["project_id"])
        # allow GET, HEAD, OPTIONS requests if user is a contributor
        if project in Project.objects.filter(users__user=request.user):
            if request.method in permissions.SAFE_METHODS:
                return True
        else:
            return request.user == project.author
        return False
