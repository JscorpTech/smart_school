from django.db import models
from django_core.models import AbstractBaseModel


class ParentOtpModel(AbstractBaseModel):
    parent = models.ForeignKey("ParentModel", on_delete=models.CASCADE)
    student = models.ForeignKey("StudentModel", on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
