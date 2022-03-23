from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CommentSerializer
from api.models import Comment, Issue, CustomUser
from django.core.exceptions import ValidationError


class CommentsViewset(ModelViewSet):
    """
    # 15 - POST /projects/{id}/issues/{id}/comments/
    # 16 - GET /projects/{id}/issues/{id}/comments/
    # 17 - PUT /projects/{id}/issues/{id}/comments/{id}/
    # 18 - DELETE /projects/{id}/issues/{id}/comments/{id}/
    # 19 - GET /projects/{id}/issues/{id}/comments/{id}/
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    # 16 - GET /projects/{id}/issues/{id}/comments/
    def list(self, request, *args, **kwargs):
        try:
            comments = Comment.objects.filter(issue=kwargs["issue_id"])
        except ValidationError:
            return Response(
                {"detail": f"{kwargs['issue_id']} is an invalid issue UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 15 - POST /projects/{id}/issues/{id}/comments/
    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                issue = Issue.objects.get(id=kwargs["issue_id"])
                author = CustomUser.objects.get(id=request.data["author"])
            except ValidationError:
                return Response(
                    {"detail": f"{kwargs['issue_id']} is an invalid issue UUID"},
                    status.HTTP_400_BAD_REQUEST,
                )
            serializer.save(issue=issue, author=author)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 17 - PUT /projects/{id}/issues/{id}/comments/{id}/
    def update(self, request, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=kwargs["comment_id"])
        except ValidationError:
            return Response(
                {"detail": f"{kwargs['comment_id']} is an invalid comment UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 18 - DELETE /projects/{id}/issues/{id}/comments/{id}/
    def destroy(self, request, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=kwargs["comment_id"])
            self.perform_destroy(comment)
        except ValidationError:
            return Response(
                {"detail": f"{kwargs['comment_id']} is an invalid comment UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        except Comment.DoesNotExist:
            return Response({"detail": "comment not found"}, status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 19 - GET /projects/{id}/issues/{id}/comments/{id}/
    def retrieve(self, request, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=kwargs["comment_id"])
        except ValidationError:
            return Response(
                {"detail": f"{kwargs['comment_id']} is an invalid comment UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        except Comment.DoesNotExist:
            return Response({"detail": "comment not found"}, status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status.HTTP_200_OK)
