from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.apps.accounts.serializers.parent import AddChildSerializer, ConfirmChildSerializer
from core.apps.accounts.services.parent import send_verification_code
from core.apps.accounts.permissions.parent import IsParent
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from core.apps.accounts.models.parent import ParentOtpModel
from rest_framework.exceptions import ValidationError, NotFound
from core.apps.accounts.serializers.users.student import ListStudentSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class ChildViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        queryset = self.request.user.parent.children.all()
        match self.action:
            case _:
                return queryset

    def get_permissions(self):
        match self.action:
            case "add_child":
                return [IsParent()]
            case _:
                return []

    def get_serializer_class(self):
        match self.action:
            case "create":
                return AddChildSerializer
            case "confirm_child":
                return ConfirmChildSerializer
            case "list":
                return ListStudentSerializer
            case _:
                return ListStudentSerializer

    def create(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        send_verification_code(request.user.parent, ser.validated_data["child"])
        return Response(data={"detail": _("Verification code sent")}, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False, url_path="confirm", url_name="confirm")
    def confirm_child(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        code = ParentOtpModel.objects.filter(
            parent=request.user.parent, student=ser.validated_data["child"], code=ser.validated_data["code"]
        )
        if not code.exists():
            raise ValidationError(detail={"code": _("invalid code")})
        code.delete()
        request.user.parent.children.add(ser.validated_data["child"])
        return Response(data={"detail": _("Child created")})

    def destroy(self, request, pk):
        child = request.user.parent.children.filter(pk=pk)
        if not child.exists():
            raise NotFound(detail=_("child not found"))
        request.user.parent.children.remove(child.first().id)
        return Response(data={"detail": _("children removed")})
