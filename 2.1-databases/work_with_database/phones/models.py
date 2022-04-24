from django.db import models
from django.db.models import CharField, ImageField, DateField, BooleanField, FloatField


class Phone(models.Model):
    name = CharField(max_length=80)
    price = FloatField()
    image = ImageField()
    release_date = DateField()
    lte_exists = BooleanField()
    slug = CharField(max_length=80)

    def __str__(self):
        return self.name
