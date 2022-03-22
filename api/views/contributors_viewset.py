from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from api.models import Contributor, Project, CustomUser
from api.serializers import ContributorListSerializer


class ContributorsViewset(ModelViewSet):
    """
    8 - POST /projects/{id}/users/
    9 - GET /projects/{id}/users/
    """

    serializer_class = ContributorListSerializer

    def get_queryset(self):
        return Contributor.objects.all()

    # 9 - GET /projects/{id}/users/
    def list(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(project=kwargs["project_id"])
        serializer = ContributorListSerializer(contributors, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 8 - POST /projects/{id}/users/
    def create(self, request, *args, **kwargs):
        serializer = ContributorListSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.get(id=kwargs["project_id"])
            user = CustomUser.objects.get(id=request.data["user"])
            serializer.save(project=project, user=user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 10 - DELETE /projects/{id}/users/{id}/
    def destroy(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs["project_id"])
        user = CustomUser.objects.get(id=kwargs["user_id"])
        contributor = Contributor.objects.filter(project=project, user=user)
        self.perform_destroy(contributor)
        return Response(status=status.HTTP_204_NO_CONTENT)
