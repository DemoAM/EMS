import time

from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import SignUpSerializer, EmployeeUserSerializer
from .permissions import IsAdmin
from .models import Role
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import LoginSerializer


class LoginAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            return Response(
                {"detail": "Successfully logged in."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    # http_method_names = ["post"]
    permission_classes = []


class UpdateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = ["patch", "delete"]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


class EmployeeUserViewSet(ModelViewSet):
    queryset = User.objects.filter(role=Role.Roles.EMPLOYEE)
    serializer_class = EmployeeUserSerializer
