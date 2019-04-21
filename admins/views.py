from django.shortcuts import render


def index(request):
    context = {'title': 'daniel huang'}
    return render(request, 'admins/index.html', context)