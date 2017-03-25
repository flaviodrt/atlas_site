from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Councilman(models.Model):

    name = models.CharField('Name', max_length=150)
    page_link = models.CharField('Page Link', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=20)
    email = models.CharField('E-mail', max_length=150)
    address = models.CharField('Address', max_length=255)
    floor = models.CharField('Floor', max_length=10)
    room = models.CharField('Room', max_length=10)
    biography = models.TextField('Biography')
    party = models.CharField('Party', max_length=10)
    picture = models.CharField('Picture', max_length=255)
    slug = models.CharField('Name', max_length=150, default=None, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
