from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class DifficultyEnum(TextChoices):
    EASY = "easy", _("Easy")
    MEDIUM = "medium", _("Medium")
    HARD = "hard", _("Hard")
