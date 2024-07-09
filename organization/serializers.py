from rest_framework import serializers
from .models import Organization
from expanse.models import Expanse


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

    def create(self, validated_data):
        from user.models import User, Role

        validated_data["user"] = User.objects.filter(role=Role.Roles.ADMIN).last()
        return Organization.objects.create(**validated_data)


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanse
        fields = "__all__"
