from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, ScienceModel, TopicModel


@receiver(post_save, sender=BobModel)
def BobSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=TopicModel)
def TopicSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=QuestionModel)
def QuestionSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=QuestionSetModel)
def QuestionsetSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ScienceModel)
def ScienceSignal(sender, instance, created, **kwargs): ...
