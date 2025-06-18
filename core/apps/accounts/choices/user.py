from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.TextChoices):
    """
    User Role Choice
    """

    ADMIN = "admin", _("Admin")
    PARENT = "parent", _("Parent")
    STUDENT = "student", _("Student")
