from rest_framework import serializers

from core.apps.school.models import QuestionSetModel
from core.apps.school.serializers.question.topic import ListTopicSerializer


class BaseQuestionsetSerializer(serializers.ModelSerializer):
    topic = ListTopicSerializer()

    class Meta:
        model = QuestionSetModel
        fields = [
            "id",
            "difficulty",
            "date",
            "topic",
        ]


class ListQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta): ...


class RetrieveQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta): ...


class CreateQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta):
        fields = [
            "id",
            "difficulty",
            "date",
            "topic",
        ]
