from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Comment, CustomUser, Issue
from api.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated


class CommentsViewset(ModelViewSet):
    """
    # 15 - POST /projects/{id}/issues/{id}/comments/
    # 16 - GET /projects/{id}/issues/{id}/comments/
    # 17 - PUT /projects/{id}/issues/{id}/comments/{id}/
    # 18 - DELETE /projects/{id}/issues/{id}/comments/{id}/
    # 19 - GET /projects/{id}/issues/{id}/comments/{id}/
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    # 16 - GET /projects/{id}/issues/{id}/comments/
    def list(self, request, *args, **kwargs):
        try:
            comments = Comment.objects.filter(issue=kwargs["issue_id"]).filter(
                issue__project__id=kwargs["project_id"]
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 15 - POST /projects/{id}/issues/{id}/comments/
    def create(self, request, *args, **kwargs):
        try:
            issue = Issue.objects.filter(project=kwargs["project_id"]).get(
                id=kwargs["issue_id"]
            )
        except Issue.DoesNotExist:
            return Response(
                {"detail": "Project does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            author = CustomUser.objects.get(id=request.data["author"])
            serializer.save(issue=issue, author=author)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 17 - PUT /projects/{id}/issues/{id}/comments/{id}/
    def update(self, request, *args, **kwargs):
        try:
            comment = (
                Comment.objects.filter(issue=kwargs["issue_id"])
                .filter(issue__project__id=kwargs["project_id"])
                .get(id=kwargs["comment_id"])
            )
        except Comment.DoesNotExist:
            return Response(
                {"detail": "Comment does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            issue = Issue.objects.get(id=kwargs["issue_id"])
            serializer.save(issue=issue)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 18 - DELETE /projects/{id}/issues/{id}/comments/{id}/
    def destroy(self, request, *args, **kwargs):
        try:
            comment = (
                Comment.objects.filter(issue=kwargs["issue_id"])
                .filter(issue__project__id=kwargs["project_id"])
                .get(id=kwargs["comment_id"])
            )
        except Comment.DoesNotExist:
            return Response(
                {"detail": "Comment does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )

        self.perform_destroy(comment)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 19 - GET /projects/{id}/issues/{id}/comments/{id}/
    def retrieve(self, request, *args, **kwargs):
        try:
            comment = (
                Comment.objects.filter(issue=kwargs["issue_id"])
                .filter(issue__project__id=kwargs["project_id"])
                .get(id=kwargs["comment_id"])
            )
        except Comment.DoesNotExist:
            return Response(
                {"detail": "Comment does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status.HTTP_200_OK)
