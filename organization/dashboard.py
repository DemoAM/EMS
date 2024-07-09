from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from user.models import Role
from expanse.models import Expanse
from .serializers import DashboardSerializer
from expanse.serializers import ExpanseSerializer
from django.db.models import Sum, Avg, Count


class DashboardView(ModelViewSet):
    queryset = Expanse.objects.all()
    serializer_class = ExpanseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        average_amount = Expanse.objects.filter(user=request.user).aggregate(
            average_amount=Avg("amount")
        )
        total_expenses = Expanse.objects.filter(user=request.user).aggregate(
            total_expenses=Sum("amount")
        )
        total_count = Expanse.objects.filter(user=request.user).aggregate(
            total_count=Count("id")
        )
        expanses = Expanse.objects.filter(user=request.user)

        expanse_serializer = ExpanseSerializer(expanses, many=True).data

        response_data = {
            "average_amount": average_amount["average_amount"],
            "total_expenses": total_expenses["total_expenses"],
            "total_count": total_count["total_count"],
            "expanses": expanse_serializer,
        }
        return Response(data=response_data)

    def get_queryset(self):
        if self.request.user.role == Role.Roles.EMPLOYEE:
            return self.queryset.filter(user=self.request.user)
        else:
            return self.queryset.all()
