from django.contrib.auth import admin
from django.contrib.admin import register
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm  # UserCreationForm,
from unfold.forms import UserChangeForm

from core.apps.accounts.models import ParentModel, StudentModel


class CustomUserAdmin(admin.UserAdmin, ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    # add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "first_name",
        "last_name",
        "phone",
        "role",
    )
    autocomplete_fields = ["groups", "user_permissions"]
    fieldsets = ((None, {"fields": ("phone",)}),) + (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class PermissionAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class GroupAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    autocomplete_fields = ("permissions",)


class SmsConfirmAdmin(ModelAdmin):
    list_display = ["phone", "code", "resend_count", "try_count"]
    search_fields = ["phone", "code"]


@register(StudentModel)
class StudentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@register(ParentModel)
class ParentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
