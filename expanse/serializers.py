from rest_framework import serializers
from .models import Expense, ExpenseCategory


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["exp_category", "amount"]
        read_only_fields = ["user", "organization", "status"]

