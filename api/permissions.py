from django.db.models import Q

from rest_framework import permissions

from .models import Comment, Contributor, Issue, Project

contrib_methods = ("POST", "GET")


class HasProjectPermission(permissions.BasePermission):
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
        try:
            project = Project.objects.get(id=view.kwargs["project_id"])
        except Project.DoesNotExist:
            return False
        # allow GET, HEAD, OPTIONS requests if user is a contributor
        if project in Project.objects.filter(users__user=request.user):
            if request.method in permissions.SAFE_METHODS:
                return True
        # allow GET, HEAD, OPTIONS, POST, DELETE if author
        if request.user == project.author:
            return True
        return False


class HasIssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            Contributor.objects.filter(project=view.kwargs["project_id"])
            .filter(user=request.user)
            .exists()
        ):
            if request.method in contrib_methods:
                return True
        if "issue_id" in view.kwargs:
            issue = Issue.objects.filter(id=view.kwargs["issue_id"])
            if issue.exists():
                return issue.first().author == request.user
        return False


class HasCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            Contributor.objects.filter(
                Q(project=view.kwargs["project_id"])
                & Q(project__issues=view.kwargs["issue_id"])
            )
            .filter(user=request.user)
            .exists()
        ):
            if request.method in contrib_methods:
                return True
        if "comment_id" in view.kwargs:
            comment = Comment.objects.filter(id=view.kwargs["comment_id"])
            if comment.exists():
                return comment.first().author == request.user
        return False
