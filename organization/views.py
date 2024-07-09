from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import OrganizationSerializer, Organization
from user.permissions import IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from expanse.models import Expanse
from .serializers import DashboardSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    http_method_names = ["get", "post"]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdmin]
