from rest_framework import serializers
from .models import Expanse, ExpanseCategory


class ExpanseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanse
        fields = ["exp_category", "amount"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        exp = Expanse.objects.create(**validated_data)
        return exp
