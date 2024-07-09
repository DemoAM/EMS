from rest_framework.viewsets import ModelViewSet
from .models import Expanse
from .serializers import ExpanseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class ExpanseViewSet(ModelViewSet):
    queryset = Expanse.objects.all()
    serializer_class = ExpanseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
