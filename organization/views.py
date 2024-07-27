from rest_framework.viewsets import ModelViewSet
from .serializers import OrganizationSerializer, Organization
from user.permissions import IsAdmin
from user.models import User, Role
from rest_framework.response import Response
from rest_framework import status


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=User.objects.filter(role=Role.Roles.ADMIN).last())
            return Response({"msg": "Your organization has been added"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




