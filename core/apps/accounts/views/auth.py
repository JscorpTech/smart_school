import uuid
from typing import Type

from core.services import UserService, SmsService
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_core import exceptions
from drf_spectacular.utils import extend_schema
from rest_framework import status, throttling, request
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet
from django_core.mixins import BaseViewSetMixin
from rest_framework.decorators import action
from ..serializers import (
    RegisterSerializer,
    ConfirmSerializer,
    ResendSerializer,
    ResetPasswordSerializer,
    ResetConfirmationSerializer,
    SetPasswordSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password
from drf_spectacular.utils import OpenApiResponse
from rest_framework.permissions import IsAuthenticated
from ..serializers import ChangePasswordSerializer, RegisterStep3Serializer
from core.apps.accounts.choices import UserStepChoice
from django.contrib.auth import hashers
from core.apps.accounts.serializers import LoginSerializer, LoginStep2Serializer
from django.contrib.auth import hashers
from rest_framework.exceptions import ValidationError
from core.apps.accounts.services.auth import create_login_token, check_login_token, delete_login_token

from .. import models


@extend_schema(tags=["register"])
class RegisterView(BaseViewSetMixin, GenericViewSet, UserService):
    throttle_classes = [throttling.UserRateThrottle]
    permission_classes = [AllowAny]
    action_permission_classes = {
        "step_3": [IsAuthenticated],
    }

    def get_serializer_class(self):
        match self.action:
            case "step_1":
                return RegisterSerializer
            case "step_2":
                return ConfirmSerializer
            case "step_3":
                return RegisterStep3Serializer
            case "resend":
                return ResendSerializer
            case _:
                return RegisterSerializer

    @extend_schema(summary="Ro'yhatdan o'tish", description="yangi userlar uchun register")
    @action(methods=["POST"], detail=False, url_path="step-1", url_name="step-1")
    def step_1(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        phone = data.get("phone")
        # Create pending user
        self.create_user(phone)
        self.send_confirmation(phone)  # Send confirmation code for sms eskiz.uz
        return Response(
            {"detail": _("Sms %(phone)s raqamiga yuborildi") % {"phone": phone}},
            status=status.HTTP_202_ACCEPTED,
        )

    @extend_schema(summary="Auth confirm.", description="To'lefon nomerni tasdiqlash sms ko'dni kiritish.")
    @action(methods=["POST"], detail=False, url_path="step-2")
    def step_2(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        phone, code = data.get("phone"), data.get("code")
        try:
            if SmsService.check_confirm(phone, code=code):
                user = get_user_model().objects.filter(phone=phone).first()
                user.step = UserStepChoice.STEP_2
                return Response(
                    data=self.validate_user(user),
                    status=status.HTTP_202_ACCEPTED,
                )
        except exceptions.SmsException as e:
            raise PermissionDenied(e)  # Response exception for APIException
        except Exception as e:
            raise PermissionDenied(e)  # Api exception for APIException

    @extend_schema(summary="Parol qo'yish", description="Yangi user uchun parol yaratish")
    @action(methods=["POST"], detail=False, url_name="step-3", url_path="step-3")
    def step_3(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        password = ser.validated_data.get("password")
        user = request.user
        user.step = UserStepChoice.STEP_3
        user.password = hashers.make_password(password)
        user.save()
        return Response(data={"detail": _("Parol yaratildi")})

    @action(methods=["POST"], detail=False, url_path="resend")
    def resend(self, rq: Type[request.Request]):
        ser = self.get_serializer(data=rq.data)
        ser.is_valid(raise_exception=True)
        phone = ser.data.get("phone")
        self.send_confirmation(phone)
        return Response({"detail": _("Sms %(phone)s raqamiga yuborildi") % {"phone": phone}})


@extend_schema(tags=["login"])
class LoginView(BaseViewSetMixin, GenericViewSet):
    permission_classes = [AllowAny]
    action_serializer_class = {
        "step_1": LoginSerializer,
        "step_2": LoginStep2Serializer,
    }

    @action(methods=["POST"], detail=False, url_name="step-1", url_path="step-1")
    def step_1(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phone = ser.validated_data.get("phone")
        password = ser.validated_data.get("password")
        user = get_user_model().objects.filter(phone=phone).first()
        if user is None or not hashers.check_password(password, user.password):
            raise ValidationError({"phone": [_("invalid user or password")]})
        service = SmsService()
        service.send_confirm(phone)
        token = create_login_token(user)
        return Response(data={"token": token}, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False, url_name="step-2", url_path="step-2")
    def step_2(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        token = ser.validated_data.get("token")
        phone = ser.validated_data.get("phone")
        code = ser.validated_data.get("code")
        user = get_user_model().objects.filter(phone=phone).first()
        if user is None:
            raise ValidationError({"phone": [_("User not found")]})
        if not check_login_token(user, token):
            raise ValidationError({"token": [_("invalid token")]})
        service = SmsService()
        try:
            service.check_confirm(phone, code)
            user_service = UserService()
            delete_login_token(token)
            return Response(data=user_service.get_token(user))
        except Exception as e:
            raise PermissionDenied(e)


@extend_schema(tags=["reset-password"])
class ResetPasswordView(BaseViewSetMixin, GenericViewSet, UserService):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        match self.action:
            case "reset_password":
                return ResetPasswordSerializer
            case "reset_confirm":
                return ResetConfirmationSerializer
            case "reset_password_set":
                return SetPasswordSerializer
            case _:
                return None

    @action(methods=["POST"], detail=False, url_path="reset-password")
    def reset_password(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phone = ser.data.get("phone")
        self.send_confirmation(phone)
        return Response({"detail": _("Sms %(phone)s raqamiga yuborildi") % {"phone": phone}})

    @action(methods=["POST"], detail=False, url_path="reset-password-confirm")
    def reset_confirm(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)

        data = ser.data
        code, phone = data.get("code"), data.get("phone")
        try:
            SmsService.check_confirm(phone, code)
            token = models.ResetToken.objects.create(
                user=get_user_model().objects.filter(phone=phone).first(),
                token=str(uuid.uuid4()),
            )
            return Response(
                data={
                    "token": token.token,
                    "created_at": token.created_at,
                    "updated_at": token.updated_at,
                },
                status=status.HTTP_200_OK,
            )
        except exceptions.SmsException as e:
            raise PermissionDenied(str(e))
        except Exception as e:
            raise PermissionDenied(str(e))

    @action(methods=["POST"], detail=False, url_path="reset-password-set")
    def reset_password_set(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        token = data.get("token")
        password = data.get("password")
        token = models.ResetToken.objects.filter(token=token)
        if not token.exists():
            raise PermissionDenied(_("Invalid token"))
        phone = token.first().user.phone
        token.delete()
        self.change_password(phone, password)
        return Response({"detail": _("password updated")}, status=status.HTTP_200_OK)


@extend_schema(tags=["me"])
class MeView(BaseViewSetMixin, GenericViewSet, UserService):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        match self.action:
            case "me":
                return UserSerializer
            case "user_update":
                return UserUpdateSerializer
            case _:
                return None

    @action(methods=["GET", "OPTIONS"], detail=False, url_path="me")
    def me(self, request):
        return Response(self.get_serializer(request.user).data)

    @action(methods=["PATCH", "PUT"], detail=False, url_path="user-update")
    def user_update(self, request):
        ser = self.get_serializer(instance=request.user, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"detail": _("Malumotlar yangilandi")})


@extend_schema(tags=["change-password"], description="Parolni o'zgartirish uchun")
class ChangePasswordView(BaseViewSetMixin, GenericViewSet):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=serializer_class,
        responses={200: OpenApiResponse(ChangePasswordSerializer)},
        summary="Change user password.",
        description="Change password of the authenticated user.",
    )
    @action(methods=["POST"], detail=False, url_path="change-password")
    def change_password(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if user.check_password(request.data["old_password"]):
            user.password = make_password(request.data["new_password"])
            user.save()
            return Response(
                data={"detail": "password changed successfully"},
                status=status.HTTP_200_OK,
            )
        raise PermissionDenied(_("invalida password"))


@extend_schema(tags=["delete-account"], summary="Accountni o'chirish")
class DeleteAccountView(BaseViewSetMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=["DELETE"], detail=False, url_name="delete_account", url_path="delete-account")
    def delete_account(self, request):
        request.user.delete()
        return Response(data={"detail": _("Account o'chirildi")})
