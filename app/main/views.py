from django.shortcuts import render


def main_page(request):
    context = {'item': 'MAIN PAGE'}
    return render(request, 'main.html', context)


def other_pages(request, menu_item):
    # print(menu_item)

    context = {'item': menu_item}
    return render(request, 'page.html', context)
