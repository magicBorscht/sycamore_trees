from django import template
from django.db import connection
from tree_menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name, path):
    nodes = list(MenuNode.objects.filter(menu_name=menu_name))
    active_node = None
    path = path.strip('/')
    menu = []
    nodelists = []
    # TODO: This whole algorithm is too clumsy and possibly needs to be rewritten
    print(len(connection.queries))
    for node in reversed(nodes):
        if node.link == path:
            active_node = node
        if node.level == 0:
            nodelists.append([node])
            nodes.remove(node)
    print(len(connection.queries))

    # TODO: Remove all references to node.parent, for it makes unwanted queries in numbers
    while nodes:
        for node in reversed(nodes):
            for nodelist in nodelists:
                if node.parent in nodelist:
                    nodelist.append(node)
                    nodes.remove(node)
                    break
            if node in nodes:
                nodes.remove(node)  # if the node is somehow parentless but has a parent (??) it will not lead us to an
                # endless loop
    print(len(connection.queries))
    for nodelist in nodelists:
        nodes.extend(nodelist)
        # We use only nodes related to the active one, and if we don't have one, we have no need to expand anything
        # if not active_node:
        #     if node.level > 0:
        #         continue
        # else:
        #     # TODO: This thing now will expand everything above the active node, including unrelated ones.
        #     # TODO: Children must be put strictly after their parents.
        #     if node.level > active_node.level:
        #         if not node.parent == active_node:
        #             continue

    for node in nodes:
        # Crude ASCII design
        name = node.name if not node.parent else '|--' * node.level + node.name
        menu.append({
            'name': name,
            'margin': node.level * 15,  # can be used instead of crude ASCII design
            'link': node.link,
        })
    print(len(connection.queries))

    return {'menu': menu}
