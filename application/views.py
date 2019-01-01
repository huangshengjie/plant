from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'name': 'huang',
               '1': 'china'}
    return render(request, 'application/index.html', context)
