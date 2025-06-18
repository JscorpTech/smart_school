from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, TopicModel


@admin.register(BobModel)
class BobAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(TopicModel)
class TopicAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(QuestionModel)
class QuestionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(QuestionSetModel)
class QuestionSetAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
