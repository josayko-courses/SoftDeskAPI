from rest_framework.viewsets import ModelViewSet

from api.models import CustomUser
from api.serializers import UserSerializer


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
