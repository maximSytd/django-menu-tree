from django.contrib import admin

from ..models import Menu
from .inlines import MenuItemInline
from apps.core.admin import BaseAdmin


@admin.register(Menu)
class MenuAdmin(BaseAdmin):
    """Admin UI for Menu model."""

    inlines = (
        MenuItemInline,
    )
    ordering = (
        "title",
    )
    list_display = (
        "title",
    )
    list_filter = (
        "title",
    )
