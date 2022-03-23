from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import CustomUser, Issue, Project
from api.serializers import IssueSerializer


class IssuesViewset(ModelViewSet):
    """
    11 - GET /projects/{id}/issues/
    12 - POST /projects/{id}/issues/
    13 - PUT /projects/{id}/issues/{id}/
    14 - DELETE /projects/{id}/issues/{id}/
    """

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()

    # 11 - GET /projects/{id}/issues/
    def list(self, request, *args, **kwargs):
        try:
            issues = Issue.objects.filter(project=kwargs["project_id"])
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 12 - POST /projects/{id}/issues/
    def create(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs["project_id"])
        except Project.DoesNotExist:
            return Response(
                {"detail": "Project does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            author = CustomUser.objects.get(id=request.data["author"])
            serializer.save(project=project, author=author)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 13 - PUT /projects/{id}/issues/{id}/
    def update(self, request, *args, **kwargs):
        try:
            issue = Issue.objects.filter(project=kwargs["project_id"]).get(
                id=kwargs["issue_id"]
            )
        except Issue.DoesNotExist:
            return Response(
                {"detail": "Issue does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = IssueSerializer(issue, data=request.data, partial=True)
        if serializer.is_valid():
            project = Project.objects.get(id=kwargs["project_id"])
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 14 - DELETE /projects/{id}/issues/{id}/
    def destroy(self, request, *args, **kwargs):
        try:
            issue = Issue.objects.filter(project=kwargs["project_id"]).get(
                id=kwargs["issue_id"]
            )
        except Issue.DoesNotExist:
            return Response(
                {"detail": "Issue does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(issue)
        return Response(status=status.HTTP_204_NO_CONTENT)
