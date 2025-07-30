from django.contrib import admin

from ..models import MenuItem
from .inlines import MenuItemInline
from apps.core.admin import BaseAdmin


@admin.register(MenuItem)
class MenuItemAdmin(BaseAdmin):
    """Admin UI for MenuItem model."""

    inlines = (
        MenuItemInline,
    )
    ordering = (
        "menu",
        "title",
    )
    list_display = (
        "title",
        "menu",
        "parent",
        "named_url",
        "url",
    )
    list_filter = (
        "menu",
    )
