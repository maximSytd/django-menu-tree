from django.contrib import admin

from ...models import MenuItem


class MenuItemInline(admin.StackedInline):
    """Represent MenuItem Admin UI Inline."""

    model = MenuItem
    extra = 1
