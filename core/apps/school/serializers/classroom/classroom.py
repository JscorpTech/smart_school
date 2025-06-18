from rest_framework import serializers

from core.apps.school.models import ClassroomModel


class BaseClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomModel
        fields = [
            "id",
            "name",
        ]


class ListClassroomSerializer(BaseClassroomSerializer):
    class Meta(BaseClassroomSerializer.Meta): ...


class RetrieveClassroomSerializer(BaseClassroomSerializer):
    class Meta(BaseClassroomSerializer.Meta): ...


class CreateClassroomSerializer(BaseClassroomSerializer):
    class Meta(BaseClassroomSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
