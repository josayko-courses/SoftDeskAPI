from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Contributor, CustomUser, Project
from api.serializers import ContributorListSerializer


class ContributorsViewset(ModelViewSet):
    """
    8 - POST /projects/{id}/users/
    9 - GET /projects/{id}/users/
    10 - DELETE /projects/{id}/users/{id}/
    """

    serializer_class = ContributorListSerializer

    def get_queryset(self):
        return Contributor.objects.all()

    # 9 - GET /projects/{id}/users/
    def list(self, request, *args, **kwargs):
        try:
            contributors = Contributor.objects.filter(project=kwargs["project_id"])
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = ContributorListSerializer(contributors, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 8 - POST /projects/{id}/users/
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
        data = {
            "user": request.data["user"],
            "project": kwargs["project_id"],
            "role": request.data["role"],
        }
        serializer = ContributorListSerializer(data=data)
        if serializer.is_valid():
            user = CustomUser.objects.get(id=data["user"])
            serializer.save(project=project, user=user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 10 - DELETE /projects/{id}/users/{id}/
    def destroy(self, request, *args, **kwargs):
        try:
            contributor = Contributor.objects.filter(project=kwargs["project_id"]).get(
                user=kwargs["user_id"]
            )
        except Contributor.DoesNotExist:
            return Response(
                {"detail": "Contributor does not exists"}, status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(
                {"detail": "Invalid id (not a number)"}, status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(contributor)
        return Response(status=status.HTTP_204_NO_CONTENT)
