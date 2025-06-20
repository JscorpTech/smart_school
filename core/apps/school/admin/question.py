from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, ScienceModel, TopicModel


@admin.register(BobModel)
class BobAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "science",
        "classroom",
    )


@admin.register(TopicModel)
class TopicAdmin(ModelAdmin):
    list_display = (
        "id",
        "bob",
        "name",
    )


@admin.register(QuestionModel)
class QuestionAdmin(ModelAdmin):
    list_display = (
        "id",
        "question_set",
    )


@admin.register(QuestionSetModel)
class QuestionSetAdmin(ModelAdmin):
    list_display = (
        "id",
        "topic",
        "difficulty",
        "date",
    )


@admin.register(ScienceModel)
class ScienceAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
