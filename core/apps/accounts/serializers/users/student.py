from rest_framework import serializers
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.accounts.models import StudentModel


class BaseStudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentModel
        fields = [
            "id",
            "user",
            "balance",
            "ball",
            "ice",
            "avatar",
        ]


class ListStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta): ...


class RetrieveStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta): ...


class CreateStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta):
        fields = [
            "id",
            "user",
            "balance",
            "ball",
            "ice",
            "avatar",
        ]
