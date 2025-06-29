from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.school.models import ClassroomModel
from core.apps.school.serializers.classroom import (
    CreateClassroomSerializer,
    ListClassroomSerializer,
    RetrieveClassroomSerializer,
)


@extend_schema(tags=["classroom"])
class ClassroomView(BaseViewSetMixin, ModelViewSet):
    queryset = ClassroomModel.objects.all()
    serializer_class = ListClassroomSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListClassroomSerializer,
        "retrieve": RetrieveClassroomSerializer,
        "create": CreateClassroomSerializer,
    }
