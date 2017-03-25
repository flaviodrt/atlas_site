from django.shortcuts import render
from councilman.models import Councilman


def index(request):
    data = {
        'councilman': Councilman.objects.all()
    }
    return render(request, 'index.html', data)


def show(request, slug):
    pass
