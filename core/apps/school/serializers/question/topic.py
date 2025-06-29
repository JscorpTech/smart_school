from rest_framework import serializers

from core.apps.school.models import TopicModel


class BaseTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = [
            "id",
            "name",
        ]


class ListTopicSerializer(BaseTopicSerializer):
    class Meta(BaseTopicSerializer.Meta): ...


class RetrieveTopicSerializer(BaseTopicSerializer):
    class Meta(BaseTopicSerializer.Meta): ...


class CreateTopicSerializer(BaseTopicSerializer):
    class Meta(BaseTopicSerializer.Meta):
        fields = [
            "id",
            "name",
            "bob",
        ]
