from modeltranslation.translator import TranslationOptions, register

from core.apps.school.models import BobModel, QuestionModel, QuestionsetModel, TopicModel


@register(BobModel)
class BobTranslation(TranslationOptions):
    fields = []


@register(TopicModel)
class TopicTranslation(TranslationOptions):
    fields = []


@register(QuestionModel)
class QuestionTranslation(TranslationOptions):
    fields = []


@register(QuestionsetModel)
class QuestionsetTranslation(TranslationOptions):
    fields = []
