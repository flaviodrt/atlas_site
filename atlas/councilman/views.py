from django.shortcuts import render, get_object_or_404
from councilman.models import Councilman


def index(request):
    data = {
        'councilmen': Councilman.objects.all().order_by('name')
    }
    return render(request, 'index.html', data)


def detail(request, slug):

    councilman = get_object_or_404(Councilman, slug=slug)
    donations = councilman.donation_set.all().order_by('-value')

    donations_sum = sum([d.value for d in donations])

    assets = councilman.asset_set.all().order_by('-value')
    assets_sum = sum([d.value for d in assets])

    data = {
        'councilman': councilman,
        'donations': donations,
        'donations_sum': donations_sum,
        'assets': assets,
        'assets_sum': assets_sum
    }
    return render(request, 'detail.html', data)
