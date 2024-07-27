from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from user.models import Role
from expanse.models import Expense
from .serializers import DashboardSerializer
from expanse.serializers import ExpenseSerializer
from django.db.models import Sum, Avg, Count


class DashboardView(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        user = request.user
        role = user.role

        if role == "employee":
            expanses = Expanse.objects.filter(user=user)
        elif role == "admin":
            expanses = Expanse.objects.filter(organization=request.user.organization)
        else:
            return Response({"MSG": "NOTHING"}, status=404)

        average_amount = expanses.aggregate(average_amount=Avg("amount"))[
            "average_amount"
        ]
        total_expenses = expanses.aggregate(total_expenses=Sum("amount"))[
            "total_expenses"
        ]
        total_count = expanses.count()

        expanse_serializer = DashboardSerializer(expanses, many=True).data

        response_data = {
            "average_amount": average_amount,
            "total_expenses": total_expenses,
            "total_count": total_count,
            "expanses": expanse_serializer,
        }
        return Response(data=response_data)

        # elif role == 'admin':
        #
        #     total_expenses_num = org_expanses.aggregate(total_expenses_num=Count("id"))["total_expenses_num"]
        #     org_total_expenses_amount = org_expanses.aggregate(total_expenses=Sum("amount"))["total_expenses"]
        #
        #     expanse_serializer = DashboardSerializer(org_expanses, many=True).data
        #     response_data = {
        #         "total_expenses_num": total_expenses_num,
        #         "org_total_expenses": org_total_expenses_amount,
        #         "expanses": expanse_serializer,
        #     }
        #     return Response(data=response_data)

    def get_queryset(self):
        if self.request.user.role == Role.Roles.EMPLOYEE:
            return self.queryset.filter(user=self.request.user)
        else:
            return self.queryset.filter(organization=self.request.user.org_name)
