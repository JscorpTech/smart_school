from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.school.models import ClassroomModel


@admin.register(ClassroomModel)
class ClassroomAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
