from rest_framework import serializers
from core.apps.accounts.models.user import User
from rest_framework.exceptions import ValidationError
from core.apps.accounts.choices.user import RoleChoice


class BaseChildSerializer(serializers.Serializer):
    def validate(self, attrs):
        user = User.objects.filter(phone=attrs["phone"])
        if not user.exists():
            raise ValidationError(detail={"phone": "User does not exist"})
        elif user.first().role != RoleChoice.STUDENT.value:
            raise ValidationError(detail={"phone": "User is not a student"})
        attrs["child"] = user.first().student
        return attrs


class AddChildSerializer(BaseChildSerializer):
    phone = serializers.CharField(max_length=20)


class ConfirmChildSerializer(BaseChildSerializer):
    code = serializers.CharField(max_length=6)
    phone = serializers.CharField(max_length=20)