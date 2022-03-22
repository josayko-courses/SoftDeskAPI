from rest_framework.viewsets import ModelViewSet

from api.models import CustomUser
from api.serializers import UserListSerializer


class UsersViewset(ModelViewSet):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
