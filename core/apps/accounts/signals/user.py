from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.apps.accounts.models.user import StudentModel

from core.apps.accounts.models import ParentModel, StudentModel


@receiver(post_save, sender=get_user_model())
def user_signal(sender, created, instance, **kwargs):
    if created and instance.username is None:
        instance.username = "U%(id)s" % {"id": 1000 + instance.id}
        instance.save()
        StudentModel.objects.create(user=instance)


@receiver(post_save, sender=StudentModel)
def StudentSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ParentModel)
def ParentSignal(sender, instance, created, **kwargs): ...
