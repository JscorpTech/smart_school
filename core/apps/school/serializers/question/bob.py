from rest_framework import serializers

from core.apps.school.models import BobModel
from core.apps.school.serializers.question.science import ListScienceSerializer
from core.apps.school.serializers.classroom.classroom import ListClassroomSerializer


class BaseBobSerializer(serializers.ModelSerializer):
    science = ListScienceSerializer()
    classroom = ListClassroomSerializer()

    class Meta:
        model = BobModel
        fields = [
            "id",
            "name",
            "science",
            "classroom",
        ]


class ListBobSerializer(BaseBobSerializer):
    class Meta(BaseBobSerializer.Meta): ...


class RetrieveBobSerializer(BaseBobSerializer):
    class Meta(BaseBobSerializer.Meta): ...


class CreateBobSerializer(BaseBobSerializer):
    class Meta(BaseBobSerializer.Meta):
        fields = [
            "id",
            "name",
            "science",
            "classroom",
        ]
