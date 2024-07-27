from user.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from expanse.models import Expense
from .models import Organization
from .serializers import AdminDashboardSerializer


class AdminDashboardView(APIView):
    permission_classes = [IsAdmin, IsAuthenticated]

    def get(self, request):
        org = Organization.objects.get(user=request.user)
        org_expenses = Expense.objects.filter(organization=org)
        pending_expenses = Expense.objects.filter(status='Pending')
        approved_expenses = Expense.objects.filter(status='Approved')
        rejected_expenses = Expense.objects.filter(status='Rejected')

        org_expenses_serializer = AdminDashboardSerializer(org_expenses, many=True)
        pending_expenses_serializer = AdminDashboardSerializer(pending_expenses, many=True)
        approved_expenses_serializer = AdminDashboardSerializer(approved_expenses, many=True)
        rejected_expenses_serializer = AdminDashboardSerializer(rejected_expenses, many=True)

        data = {
            "org_expenses": org_expenses_serializer.data,
            "pending_expenses": pending_expenses_serializer.data,
            "approved_expenses": approved_expenses_serializer.data,
            "rejected_expenses": rejected_expenses_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            expense = Expense.objects.get(id=id, status="Pending")
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found or not pending"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdminDashboardSerializer(expense, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
