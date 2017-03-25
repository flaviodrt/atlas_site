from django.shortcuts import render, get_object_or_404
from councilman.models import Councilman


def index(request):
    data = {
        'councilmen': Councilman.objects.all().order_by('name')
    }
    return render(request, 'index.html', data)


def detail(request, slug):
    data = {
        'councilman': get_object_or_404(Councilman, slug=slug)
    }
    return render(request, 'detail.html', data)
