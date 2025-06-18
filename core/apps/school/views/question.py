from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.school.models import BobModel, QuestionModel, QuestionsetModel, TopicModel
from core.apps.school.serializers.question import (
    CreateBobSerializer,
    CreateQuestionSerializer,
    CreateQuestionsetSerializer,
    CreateTopicSerializer,
    ListBobSerializer,
    ListQuestionSerializer,
    ListQuestionsetSerializer,
    ListTopicSerializer,
    RetrieveBobSerializer,
    RetrieveQuestionSerializer,
    RetrieveQuestionsetSerializer,
    RetrieveTopicSerializer,
)


@extend_schema(tags=["bob"])
class BobView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BobModel.objects.all()
    serializer_class = ListBobSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBobSerializer,
        "retrieve": RetrieveBobSerializer,
        "create": CreateBobSerializer,
    }


@extend_schema(tags=["topic"])
class TopicView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TopicModel.objects.all()
    serializer_class = ListTopicSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTopicSerializer,
        "retrieve": RetrieveTopicSerializer,
        "create": CreateTopicSerializer,
    }


@extend_schema(tags=["question"])
class QuestionView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListQuestionSerializer,
        "retrieve": RetrieveQuestionSerializer,
        "create": CreateQuestionSerializer,
    }


@extend_schema(tags=["questionSet"])
class QuestionsetView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = QuestionsetModel.objects.all()
    serializer_class = ListQuestionsetSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListQuestionsetSerializer,
        "retrieve": RetrieveQuestionsetSerializer,
        "create": CreateQuestionsetSerializer,
    }
