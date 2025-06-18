from rest_framework import serializers

from core.apps.school.models import BobModel


class BaseBobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BobModel
        fields = [
            "id",
            "name",
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
        ]
