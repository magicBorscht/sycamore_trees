from django import template
from django.db import connection
from tree_menu.models import MenuNode
from django.shortcuts import reverse
from django.shortcuts import resolve_url
from django.urls.exceptions import NoReverseMatch

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name, path):
    nodes = list(MenuNode.objects.filter(menu_name=menu_name).order_by('level'))
    active_node = None
    menu = []
    nodes_to_operate = []
    print(len(connection.queries))
    for node in reversed(nodes):
        if node.link == path or node.link == path.strip('/'):
            active_node = node
        if not node.parent_id:
            nodes_to_operate.append(node)
    print(len(connection.queries))

    if active_node:
        active_family_tree = active_node.get_family_tree(nodes)

        for node in nodes:
            if not node.parent_id:
                continue
            if node.parent_id not in active_family_tree:
                continue
            for i, other_node in enumerate(nodes_to_operate):
                if node.parent_id == other_node.pk:
                    nodes_to_operate.insert(i+1, node)
                    break

    print(len(connection.queries))
    # for nodelist in nodelists:
    for node in nodes_to_operate:
        # Crude ASCII design
        name = node.name if not node.parent_id else '|--' * node.level + node.name
        try:
            reverse(node.link)
            named_link = True
        except NoReverseMatch:
            named_link = False
        menu.append({
            'name': name,
            'margin': node.level * 15,  # can be used instead of crude ASCII design
            'named_link': named_link,
            'link': node.link,
        })

    print(len(connection.queries))

    return {'menu': menu}
