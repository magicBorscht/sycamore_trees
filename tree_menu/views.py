from django.shortcuts import render


def what_a_view(request):
    context = {
        'woah': 'A wisdom of the ages'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def not_a_view(request):
    context = {
        'woah': 'You can never be aware enough'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def view_is_gone(request):
    context = {
        'woah': 'The lock, stock and barrel of it all is the County Council'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def policeman_fox(request):
    context = {
        'woah': 'I really can use this app to tell more about myself'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def about_myself(request):
    context = {
        'woah': 'I will think of something to tell you about myself, maybe I will do it right here. '
                'Now I can tell only that I love music and surrealism.'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def one_more_view(request):
    context = {
        'woah': 'The owls are not what they seem.'
    }
    return render(request, 'tree_menu/basic_template.html', context)
