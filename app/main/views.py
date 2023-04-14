from django.shortcuts import render


def main_page(request):
    context = {'path': 'MAIN PAGE'}
    return render(request, 'main.html', context)


def other_pages(request, my_path):
    context = {'path': my_path}
    return render(request, 'main.html', context)
