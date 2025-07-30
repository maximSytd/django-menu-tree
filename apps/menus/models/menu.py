
from django.db import models

from apps.core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Menu(BaseModel):
    """Represent Menu in db."""

    title = models.CharField(
        max_length=120,
        unique=True,
        verbose_name=_("Title"),
    )

    def __str__(self):
        return f"{self.title}"