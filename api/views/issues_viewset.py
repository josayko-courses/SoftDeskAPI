from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from api.models import Issue, Project, CustomUser
from api.serializers import IssueSerializer
from django.core.exceptions import ValidationError


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
                {
                    "detail": f"{kwargs['project_id']} is an invalid project id (expected a number)"
                },
                status.HTTP_400_BAD_REQUEST,
            )
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 12 - POST /projects/{id}/issues/
    def create(self, request, *args, **kwargs):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            try:
                project = Project.objects.get(id=kwargs["project_id"])
            except ValueError:
                return Response(
                    {
                        "detail": f"{kwargs['project_id']} is an invalid project id (expected a number)"
                    },
                    status.HTTP_400_BAD_REQUEST,
                )
            author = CustomUser.objects.get(id=request.data["author"])
            serializer.save(project=project, author=author)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 13 - PUT /projects/{id}/issues/{id}/
    def update(self, request, *args, **kwargs):
        try:
            issue = Issue.objects.get(id=kwargs["issue_id"])
        except:
            return Response(
                {"detail": f"{kwargs['issue_id']} is an invalid issue UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        serializer = IssueSerializer(issue, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 14 - DELETE /projects/{id}/issues/{id}/
    def destroy(self, request, *args, **kwargs):
        try:
            issue = Issue.objects.get(id=kwargs["issue_id"])
            self.perform_destroy(issue)
        except ValidationError:
            return Response(
                {"detail": f"{kwargs['issue_id']} is an invalid issue UUID"},
                status.HTTP_400_BAD_REQUEST,
            )
        except Issue.DoesNotExist:
            return Response({"errors": "Not Found"}, status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
