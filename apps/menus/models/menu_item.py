from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class MenuItem(BaseModel):
    """Represent MenuItem in db."""

    DEFAULT_URL = "#"

    menu = models.ForeignKey(
        to="menus.Menu",
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name=_("Menu"),
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_("Title"),
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("Parent"),
    )
    named_url = models.CharField(
        max_length=120,
        blank=True,
        verbose_name=_("Named url"),
        default=DEFAULT_URL,
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Url"),
        default=DEFAULT_URL,
    )

    def get_absolute_url(self) -> str:
        """Return absolute url to which the menu item is transferred."""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.DEFAULT_URL
        return self.url or self.DEFAULT_URL

    def __str__(self):
        return f"{self.title}"
