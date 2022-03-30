from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import CustomUser
from api.serializers import UserCreateSerializer, UserListSerializer


class UsersViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer
    detail_serializer_class = UserCreateSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create_user(
                email=request.data["email"],
                password=request.data["password"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
            )
            return Response(
                {"email": serializer.data["email"]},
                status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == "post":
            return self.detail_serializer_class
        return super().get_serializer_class()
