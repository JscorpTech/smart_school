from modeltranslation.translator import TranslationOptions, register

from core.apps.school.models import ClassroomModel


@register(ClassroomModel)
class ClassroomTranslation(TranslationOptions):
    fields = []
