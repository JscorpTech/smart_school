from django_filters import rest_framework as filters

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, TopicModel


class BobFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = BobModel
        fields = [
            "name",
        ]


class TopicFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TopicModel
        fields = [
            "name",
        ]


class QuestionFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = QuestionModel
        fields = [
            "name",
        ]


class QuestionsetFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = QuestionSetModel
        fields = [
            "name",
        ]
