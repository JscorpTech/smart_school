from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.school.enums.question import DifficultyEnum


class BobModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "bob"
        verbose_name = _("BobModel")
        verbose_name_plural = _("BobModels")


class TopicModel(AbstractBaseModel):
    bob = models.ForeignKey("BobModel", verbose_name=_("bob"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            bob=BobModel._create_fake(),
        )

    class Meta:
        db_table = "topic"
        verbose_name = _("TopicModel")
        verbose_name_plural = _("TopicModels")


class QuestionSetModel(AbstractBaseModel):
    topic = models.ForeignKey("TopicModel", verbose_name=_("topic"), on_delete=models.CASCADE)
    difficulty = models.CharField(verbose_name=_("difficulty"), max_length=255, choices=DifficultyEnum.choices)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    date = models.DateField(verbose_name=_("date"))

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            topic=TopicModel._create_fake(),
            difficulty=DifficultyEnum.EASY,
            date="2022-01-01",
        )

    class Meta:
        db_table = "questionset"
        verbose_name = _("QuestionsetModel")
        verbose_name_plural = _("QuestionsetModels")


class QuestionModel(AbstractBaseModel):
    question_set = models.ForeignKey("QuestionSetModel", verbose_name=_("question_set"), on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            question_set=QuestionSetModel._create_fake(),
        )

    class Meta:
        db_table = "question"
        verbose_name = _("QuestionModel")
        verbose_name_plural = _("QuestionModels")
