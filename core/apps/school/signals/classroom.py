from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.school.models import ClassroomModel


@receiver(post_save, sender=ClassroomModel)
def ClassroomSignal(sender, instance, created, **kwargs): ...
