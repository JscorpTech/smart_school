from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import exceptions, serializers


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class LoginStep2Serializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    token = serializers.CharField(max_length=50)
    code = serializers.IntegerField()


class RegisterStep3Serializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")
        if password is None:
            raise exceptions.ValidationError({"phone": _("telefon raqam majburiy")})
        elif password != password_confirm:
            raise exceptions.ValidationError({"phone": _("confirm password birxil emas")})
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = get_user_model().objects.filter(phone=value, validated_at__isnull=False)
        if user.exists():
            raise exceptions.ValidationError(_("Phone number already registered."), code="unique")
        return value

    class Meta:
        model = get_user_model()
        fields = ["phone"]


class ConfirmSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = get_user_model().objects.filter(phone=value)
        if user.exists():
            return value

        raise serializers.ValidationError(_("User does not exist"))


class ResetConfirmationSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = get_user_model().objects.filter(phone=value)
        if user.exists():
            return value
        raise serializers.ValidationError(_("User does not exist"))


class ResendSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
