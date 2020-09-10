from django import template
from tree_menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name, path):
    nodes = list(MenuNode.objects.filter(menu_name=menu_name))
    active_node = None
    path = path.strip('/')
    for node in nodes:
        if node.link == path:
            active_node = node
            break

    menu = []
    for node in nodes:
        # We use only nodes related to the active one, and if we don't have one, we have no need to expand anything
        if not active_node:
            if node.level > 0:
                continue
        else:
            if node.level > active_node.level:
                if not node.parent == active_node or node.parent == active_node.parent:
                    continue

        # Crude ASCII design
        name = node.name if not node.parent else '|--' * node.level + node.name
        menu.append({
            'name': name,
            'margin': node.level * 15,  # can be used instead of crude ASCII design
            'link': node.link,
        })

    return {'menu': menu}
