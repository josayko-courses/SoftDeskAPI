from django.db.models import Q

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Project
from api.permissions import HasProjectPermission
from api.serializers import ProjectDetailSerializer, ProjectListSerializer


class ProjectsViewset(ModelViewSet):
    """
    3 - GET /projects/
    4 - POST /projects/
    5 - GET /projects/{id}/
    6 - PUT /projects/{id}/
    7 - DELETE /projects/{id}/
    """

    permission_classes = (IsAuthenticated, HasProjectPermission)
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        contributions = Project.objects.filter(
            Q(author=request.user) | Q(users__user=request.user)
        ).distinct()
        serializer = ProjectListSerializer(contributions, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            contribution = (
                Project.objects.filter(
                    Q(author=request.user) | Q(users__user=request.user)
                )
                .distinct()
                .get(users__project=kwargs["project_id"])
            )
        except Project.DoesNotExist:
            return Response(
                {"detail": "Project does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = ProjectDetailSerializer(contribution)
        return Response(serializer.data, status.HTTP_200_OK)
