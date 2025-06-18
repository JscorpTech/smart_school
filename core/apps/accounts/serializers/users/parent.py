from rest_framework import serializers
from core.apps.accounts.models import ParentModel
from core.apps.accounts.serializers.user import UserSerializer


class BaseParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ParentModel
        fields = [
            "id",
            "user",
        ]


class ListParentSerializer(BaseParentSerializer):
    class Meta(BaseParentSerializer.Meta): ...


class RetrieveParentSerializer(BaseParentSerializer):
    class Meta(BaseParentSerializer.Meta): ...


class CreateParentSerializer(BaseParentSerializer):
    class Meta(BaseParentSerializer.Meta):
        fields = [
            "id",
            "user",
        ]
