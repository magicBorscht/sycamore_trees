from django.shortcuts import render


def what_a_view(request):
    context = {
        'message': 'Hello there'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def not_a_view(request):
    context = {
        'message': 'This is my sample text, the creation I am truly proud of'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def view_is_gone(request):
    context = {
        'message': 'The lock, stock and barrel of it all is the County Council'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def policeman_fox(request):
    context = {
        'message': 'I really can use this app to tell more about myself.'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def about_myself(request):
    context = {
        'message': 'So I am the person who did all this. I am a web developer and I love Python, music and surrealism.'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def one_more_view(request):
    context = {
        'message': 'The owls are not what they seem.'
    }
    return render(request, 'tree_menu/basic_template.html', context)


def and_another_view(request):
    context = {
        'message': 'The Party requires more views, comrade!'
    }
    return render(request, 'tree_menu/basic_template.html', context)
