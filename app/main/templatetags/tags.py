from django import template
from main.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, text):
    if text == 'main_menu':
        menu_items = Menu.objects.filter(level=1)
    else:
        res = ''
        print(f"!!!!!!!!!!!!!  {type(context)}      !!!!!!!!!!!!!!!!!!")
        for c in context:
            try:
                print(f'---------  {c}  ---------')
                res = c['item']
                break
            except:
                print('========')
        print(res)
        item = Menu.objects.get(name=res)
        print(item)
        print(item.url)
        print(item.parent)
        childs = Menu.objects.filter(parent=item)
        menu_items = [item.parent, item]
        for c in childs:
            menu_items.append(c)
        print(menu_items)
    return {
        "menu_items": menu_items,
    }



