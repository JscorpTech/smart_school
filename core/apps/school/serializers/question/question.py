from rest_framework import serializers

from core.apps.school.models import QuestionModel


class BaseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = [
            "id",
            "name",
        ]


class ListQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta): ...


class RetrieveQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta): ...


class CreateQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
