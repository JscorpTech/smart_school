from modeltranslation.translator import TranslationOptions, register

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, ScienceModel, TopicModel


@register(BobModel)
class BobTranslation(TranslationOptions):
    fields = []


@register(TopicModel)
class TopicTranslation(TranslationOptions):
    fields = []


@register(QuestionModel)
class QuestionTranslation(TranslationOptions):
    fields = []


@register(QuestionSetModel)
class QuestionsetTranslation(TranslationOptions):
    fields = []


@register(ScienceModel)
class ScienceTranslation(TranslationOptions):
    fields = []
