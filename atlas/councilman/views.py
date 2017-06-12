from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from django.http import JsonResponse
from councilman.models import Councilman


def index(request):
    return render(request, 'index.html')


def detail(request, slug):

    councilman = get_object_or_404(Councilman, slug=slug)

    election_expenses = list(
        councilman.expenseselection_set.all()
        .values('kind').annotate(Sum('value')).order_by('-value__sum')
    )

    votes = councilman.vote_set.get(election_year=2016)

    data = {
        'councilman': councilman,
        'votes': votes,
        'election_expenses': election_expenses
    }
    return render(request, 'detail.html', data)


def treemap(request):
    content = [
        dict(name='Partidos', parent='', size=None)
    ]
    parties = [
        dict(name="{0}".format(c['party']), parent="Partidos", party="Partidos", size=None)
        for c in Councilman.objects.values('party').distinct()
    ]
    parties.append(
        dict(name="Todos", parent="Partidos", party="Partidos", size=None)
    )
    councilmen = [
        dict(name="{0}".format(c.name), slug="{0}".format(c.slug),
             party="{0}".format(c.party),
             parent="Todos", size=1, donations=c.donation_sum(),
             assets=c.asset_sum(),
             election_expenses=c.election_expense_sum(),
             expenses=c.expense_sum())
        for c in Councilman.objects.all()
    ]

    content.extend(parties)
    content.extend(councilmen)

    return JsonResponse(content, safe=False)
