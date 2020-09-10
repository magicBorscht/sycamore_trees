from django import template
from tree_menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name, path):
    nodes = list(MenuNode.objects.filter(menu_name=menu_name))

    menu = []
    for node in nodes:
        name = node.name if not node.parent else '|--' * node.level + node.name
        menu.append({
            'name': name,
            'margin': node.level * 15,
            'link': 'page',
        })

    return {'menu': menu}
