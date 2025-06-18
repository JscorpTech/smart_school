from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class DifficultyEnum(TextChoices):
    EASY = "EASY", _("Easy")
    MEDIUM = "MEDIUM", _("Medium")
    HARD = "HARD", _("Hard")
