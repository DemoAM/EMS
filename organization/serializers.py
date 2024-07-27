from rest_framework import serializers
from .models import Organization
from expanse.models import Expense


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "organization_name",
            "description",
            "address",
            "organization_type",
            "no_employees",
        ]
        read_only_fields = ["user"]

    def validated_organization_name(self, value):
        return value.strip().upper()


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class AdminDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ["user","organization","exp_category","amount"]

