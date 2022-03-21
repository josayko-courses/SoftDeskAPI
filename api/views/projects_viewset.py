from rest_framework.viewsets import ModelViewSet

from api.models import Project
from api.serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectsViewset(ModelViewSet):
    """
    3 - GET /projects/
    4 - POST /projects/
    5 - GET /projects/{id}/
    6 - PUT /projects/{id}/
    7 - DELETE /projects/{id}/
    """

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
