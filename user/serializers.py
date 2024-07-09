from rest_framework import serializers

from user.models import User
from user.models import Role
from organization.models import Organization


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "email", "password"]

        read_only_fields = [
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        ]

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        validated_data["role"] = Role.Roles.ADMIN
        user = User.objects.create_user(**validated_data)
        return user


class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "email", "password"]
        read_only_fields = [
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "org_name",
            "role",
        ]

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        validated_data["role"] = Role.Roles.EMPLOYEE
        org = Organization.objects.get(user=self.context["request"].user)
        validated_data["org_name"] = org

        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            from django.contrib.auth import authenticate

            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            if not user:
                raise serializers.ValidationError("Invalid login credentials.")
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        data["user"] = user
        return data
