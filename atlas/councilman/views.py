from django.shortcuts import render, get_object_or_404
from councilman.models import Councilman
from django.db.models import Sum

def index(request):
    data = {
        'councilmen': Councilman.objects.all().order_by('name')
    }
    return render(request, 'index.html', data)


def detail(request, slug):

    councilman = get_object_or_404(Councilman, slug=slug)
    donations = councilman.donation_set.all().order_by('-value')

    assets = councilman.asset_set.all().order_by('-value')

    expenses = councilman.expense_set.all().order_by('-value')

    election_expenses = list(
        councilman.expenseselection_set.all()
        .values('kind').annotate(Sum('value')).order_by('-value__sum')
    )

    votes = councilman.vote_set.get(election_year=2016)

    data = {
        'councilman': councilman,
        'donations': donations,
        'assets': assets,
        'expenses': expenses,
        'votes': votes,
        'election_expenses': election_expenses
    }
    return render(request, 'detail.html', data)
