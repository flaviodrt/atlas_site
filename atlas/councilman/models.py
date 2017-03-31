from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Councilman(models.Model):

    name = models.CharField('Name', max_length=150)
    page_link = models.CharField('Page Link', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=50)
    email = models.CharField('E-mail', max_length=150)
    address = models.CharField('Address', max_length=255)
    floor = models.CharField('Floor', max_length=10)
    room = models.CharField('Room', max_length=10)
    biography = models.TextField('Biography')
    party = models.CharField('Party', max_length=10)
    picture = models.CharField('Picture', max_length=255)
    slug = models.CharField('Name', max_length=150, default=None, null=True)
    sequential_id = models.BigIntegerField('Sequential Id', default=None, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Donation(models.Model):

    councilman = models.ForeignKey(Councilman)
    sequential_id = models.BigIntegerField('Sequential Id', null=True)
    state = models.CharField('State', max_length=50)
    candidate = models.CharField('Candidate', max_length=150)
    donor = models.CharField('Donor', max_length=255)
    donor_tax_name = models.CharField('Donor Tax Name', max_length=255)
    economic_sector = models.CharField('Economic Sector', max_length=100)
    value = models.DecimalField('Value', max_digits=19, decimal_places=2)
    type = models.CharField('Type', max_length=150)
    description = models.CharField('Description', max_length=255)

