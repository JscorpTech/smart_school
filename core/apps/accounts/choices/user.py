from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.TextChoices):
    """
    User Role Choice
    """

    ADMIN = "admin", _("Admin")
    PARENT = "parent", _("Parent")
    STUDENT = "student", _("Student")


class UserStepChoice(models.TextChoices):
    STEP_1 = "step1", _("step 1")
    STEP_2 = "step2", _("step 2")
    STEP_3 = "step3", _("step 3")
