from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import ParentModel, StudentModel
from core.apps.accounts.serializers.users import (
    CreateParentSerializer,
    CreateStudentSerializer,
    ListParentSerializer,
    ListStudentSerializer,
    RetrieveParentSerializer,
    RetrieveStudentSerializer,
)


@extend_schema(tags=["student"])
class StudentView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = ListStudentSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListStudentSerializer,
        "retrieve": RetrieveStudentSerializer,
        "create": CreateStudentSerializer,
    }


@extend_schema(tags=["parent"])
class ParentView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ParentModel.objects.all()
    serializer_class = ListParentSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListParentSerializer,
        "retrieve": RetrieveParentSerializer,
        "create": CreateParentSerializer,
    }
