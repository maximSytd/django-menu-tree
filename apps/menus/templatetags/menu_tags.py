from django import template
from django.db import models
from django.utils.safestring import mark_safe, SafeText

from ..models import Menu, MenuItem
from ..utils.menu import build_menu_tree, render_menu_html


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context: dict, menu_title: str) -> SafeText:
    """Return templatetag of menu tree items."""
    try:
        return mark_safe(
            render_menu_html(
                tree=build_menu_tree(
                    MenuItem.objects.select_related(
                        "menu",
                        "parent",
                    ).filter(
                        menu__title=menu_title,
                    ),
                ),
                current_path=context["request"].path,
            ),
        )
    except Menu.DoesNotExist:
        return ""
