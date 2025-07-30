import typing

from django.db.models import QuerySet

from ..models import MenuItem


MenuTree: typing.TypeAlias = list["MenuNode"]

class MenuNode(typing.TypedDict):
    """Represent typed dict of menu node that contains MenuItem's."""

    item: MenuItem
    children: list["MenuNode"]


def build_menu_tree(items: QuerySet[MenuItem]) -> MenuTree:
    """Return and build tree from menu children."""
    tree = []
    lookup = {}

    for item in items:
        lookup.setdefault(item.id, {"item": item, "children": []})
    for item in items:
        if item.parent:
            lookup[item.parent_id]["children"].append(lookup[item.id])
        else:
            tree.append(lookup[item.id])
    return tree

def render_menu_html(
    tree: MenuTree,
    current_path: str,
    level: int = 0,
    active_path: None | str = None,
) -> str:
    """Return html ul tag of menu tree."""
    html = "<ul>"
    for node in tree:
        item = node["item"]
        url = item.get_absolute_url()
        is_active = current_path == url or (
            active_path and item.id in active_path
        )
        children_html = ""

        if node["children"]:
            children_html = render_menu_html(
                tree=node["children"],
                current_path=current_path,
                level=level + 1,
                active_path=active_path,
            )

        css_class = "active" if is_active else ""
        html += (
            f"<li class='{css_class}'><a href='{url}'>{item.title}</a>"
            f"{children_html}</li>"
        )
    html += "</ul>"
    return html


