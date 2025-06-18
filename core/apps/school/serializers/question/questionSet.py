from rest_framework import serializers

from core.apps.school.models import QuestionSetModel


class BaseQuestionsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSetModel
        fields = [
            "id",
            "name",
        ]


class ListQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta): ...


class RetrieveQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta): ...


class CreateQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
