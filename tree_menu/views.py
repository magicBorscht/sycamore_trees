from django.shortcuts import render


def what_a_view(request):
    return render(request, 'tree_menu/basic_template.html')
