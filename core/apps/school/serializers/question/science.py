from rest_framework import serializers

from core.apps.school.models import ScienceModel


class BaseScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceModel
        fields = [
            "id",
            "name",
        ]


class ListScienceSerializer(BaseScienceSerializer):
    class Meta(BaseScienceSerializer.Meta): ...


class RetrieveScienceSerializer(BaseScienceSerializer):
    class Meta(BaseScienceSerializer.Meta): ...


class CreateScienceSerializer(BaseScienceSerializer):
    class Meta(BaseScienceSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
