from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.models import Project
from api.serializers import ProjectDetailSerializer, ProjectListSerializer


class ProjectsViewset(ModelViewSet):
    """
    3 - GET /projects/
    4 - POST /projects/
    5 - GET /projects/{id}/
    6 - PUT /projects/{id}/
    7 - DELETE /projects/{id}/
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
