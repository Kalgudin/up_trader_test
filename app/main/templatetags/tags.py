from django import template
from main.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, tag):
    url = context.request.path
    if url == '/':
        menu_items = Menu.objects.filter(level=1, tag=tag)
    else:
        try:
            item = Menu.objects.get(url=url, tag=tag)
            menu_items = [item]
            if item.parent: _get_parents(menu_items)
            _get_children(menu_items)
        except:
            menu_items = []
    return {
        "menu_items": menu_items,
    }


def _get_parents(items_list):
    parent = items_list[0].parent
    items_list.insert(0, parent)
    if parent.level > 1:
        _get_parents(items_list)
    else:
        return items_list


def _get_children(items_list):
    parent = items_list[-1]
    children = Menu.objects.filter(parent=parent)
    for child in children:
        items_list.append(child)
