from rest_framework import serializers

from core.apps.school.models import QuestionModel
from core.apps.school.serializers.question.questionset import ListQuestionsetSerializer


class BaseQuestionSerializer(serializers.ModelSerializer):
    question_set = ListQuestionsetSerializer()

    class Meta:
        model = QuestionModel
        fields = [
            "id",
            "question_set",
        ]


class ListQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta): ...


class RetrieveQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta): ...


class CreateQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta):
        fields = [
            "id",
            "question_set",
        ]
