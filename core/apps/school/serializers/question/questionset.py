from rest_framework import serializers

from core.apps.school.models import QuestionSetModel
from core.apps.school.serializers.question.topic import ListTopicSerializer
from core.apps.school.serializers.question.science import ListScienceSerializer
from core.apps.school.serializers.classroom.classroom import ListClassroomSerializer


class BaseQuestionsetSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()
    science = serializers.SerializerMethodField()

    def get_classroom(self, instance) -> ListClassroomSerializer:
        return ListClassroomSerializer(instance.topic.bob.classroom).data

    def get_science(self, instance) -> ListScienceSerializer:
        return ListScienceSerializer(instance.topic.bob.science).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["topic"] = ListTopicSerializer(instance.topic).data
        return data

    class Meta:
        model = QuestionSetModel
        fields = [
            "id",
            "difficulty",
            "date",
            "topic",
            "classroom",
        ]


class ListQuestionsetSerializer(BaseQuestionsetSerializer):
    topic = ListTopicSerializer()

    class Meta(BaseQuestionsetSerializer.Meta): ...


class RetrieveQuestionsetSerializer(BaseQuestionsetSerializer):
    topic = ListTopicSerializer()

    class Meta(BaseQuestionsetSerializer.Meta): ...


class CreateQuestionsetSerializer(BaseQuestionsetSerializer):
    class Meta(BaseQuestionsetSerializer.Meta):
        fields = [
            "id",
            "difficulty",
            "date",
            "topic",
        ]
