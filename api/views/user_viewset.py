from rest_framework.viewsets import ModelViewSet

from api.serializers import UserSerializer
from api.models import CustomUser


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
