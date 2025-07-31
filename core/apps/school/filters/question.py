from django_filters import rest_framework as filters

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, ScienceModel, TopicModel


class BobFilter(filters.FilterSet):

    class Meta:
        model = BobModel
        fields = [
            "name",
        ]


class TopicFilter(filters.FilterSet):

    class Meta:
        model = TopicModel
        fields = [
            "name",
        ]


class QuestionFilter(filters.FilterSet):

    class Meta:
        model = QuestionModel
        fields = [
            "name",
        ]


class QuestionsetFilter(filters.FilterSet):

    class Meta:
        model = QuestionSetModel
        fields = [
            "name",
        ]


class ScienceFilter(filters.FilterSet):

    class Meta:
        model = ScienceModel
        fields = [
            "name",
        ]
