from modeltranslation.translator import TranslationOptions, register

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, ScienceModel, TopicModel


@register(BobModel)
class BobTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(TopicModel)
class TopicTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(QuestionModel)
class QuestionTranslation(TranslationOptions):
    fields = []


@register(QuestionSetModel)
class QuestionsetTranslation(TranslationOptions):
    fields = []


@register(ScienceModel)
class ScienceTranslation(TranslationOptions):
    fields = [
        "name",
    ]
