from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MenuAppConfig(AppConfig):
    """Default configuration for Menus app."""

    name = "apps.menus"
    verbose_name = _("Menus")
