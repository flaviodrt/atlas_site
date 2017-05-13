from django.contrib import admin
from .models import Councilman, Donation, Expense, Asset, Vote, Salary,
    ExpensesElection

admin.site.register(Councilman)
admin.site.register(Donation)
admin.site.register(Expense)
admin.site.register(Asset)
admin.site.register(Vote)
admin.site.register(Salary)
admin.site.register(ExpensesElection)
