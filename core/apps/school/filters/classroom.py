from django_filters import rest_framework as filters

from core.apps.school.models import ClassroomModel


class ClassroomFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ClassroomModel
        fields = [
            "name",
        ]
