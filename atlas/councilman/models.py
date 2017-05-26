from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Councilman(models.Model):

    STATUS_CHOICES = (
        (0, 'Inativo'),
        (1, 'Ativo')
    )

    name = models.CharField('Name', max_length=150)
    page_link = models.CharField('Page Link', max_length=100, default=None, null=True)
    phone_number = models.CharField('Phone Number', max_length=50, default=None, null=True)
    email = models.CharField('E-mail', max_length=150, default=None, null=True)
    address = models.CharField('Address', max_length=255, default=None, null=True)
    floor = models.CharField('Floor', max_length=10, default=None, null=True)
    room = models.CharField('Room', max_length=10, default=None, null=True)
    biography = models.TextField('Biography', default=None, null=True)
    party = models.CharField('Party', max_length=10, default=None, null=True)
    picture = models.CharField('Picture', max_length=255, default=None, null=True)
    slug = models.CharField('Name', max_length=150, default=None, null=True)
    sequential_id = models.BigIntegerField('Sequential Id', default=None, null=True)
    status = models.IntegerField('Status', choices=STATUS_CHOICES, default=1)

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Donation(models.Model):

    councilman = models.ForeignKey(Councilman)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)
    state = models.CharField('State', max_length=50)
    candidate = models.CharField('Candidate', max_length=150)
    donor = models.CharField('Donor', max_length=255)
    donor_tax_name = models.CharField('Donor Tax Name', max_length=255)
    economic_sector = models.CharField('Economic Sector', max_length=100)
    value = models.DecimalField('Value', max_digits=19, decimal_places=2)
    kind = models.CharField('Type', max_length=150)
    description = models.CharField('Description', max_length=255)

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)


class Expense(models.Model):

    councilman = models.ForeignKey(Councilman)
    date = models.DateField('Date')
    department = models.CharField('Department', max_length=255)
    expense = models.CharField('Expense', max_length=255)
    value = models.DecimalField('Value', max_digits=19, decimal_places=2)
    provider = models.CharField('Provider', max_length=255)
    cnpj = models.CharField('Tax ID', max_length=255)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)


class Asset(models.Model):

    councilman = models.ForeignKey(Councilman)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)
    kind = models.CharField('Type', max_length=150)
    description = models.CharField('Description', max_length=255)
    value = models.DecimalField('Value', max_digits=19, decimal_places=2)
    election_year = models.IntegerField('Election Year')

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)


class Vote(models.Model):

    councilman = models.ForeignKey(Councilman)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)
    votes = models.IntegerField('Votes')
    election_year = models.IntegerField('Election Year')

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)


class Salary(models.Model):

    councilman = models.ForeignKey(Councilman, null=True)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)

    sector = models.IntegerField('Sector')
    name = models.IntegerField('Name')
    role = models.IntegerField('Role')
    gross_salary = models.IntegerField('Gross Salary')
    net_salary = models.IntegerField('Net Salary')
    as_of = models.IntegerField('As Of')
    link = models.IntegerField('Link')
    download_time = models.IntegerField('Download Time')

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)


class ExpensesElection(models.Model):
    councilman = models.ForeignKey(Councilman)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)
    provider = models.CharField('Provider', max_length=255)
    cnpj = models.CharField('Tax ID', max_length=255)
    economic_sector = models.CharField('Economic Sector', max_length=255)
    value = models.IntegerField('Value')
    kind = models.CharField('Kind', max_length=255)
    description = models.CharField('Description', max_length=255)

    from_file = models.CharField('From file', max_length=255, default=None, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
