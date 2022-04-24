import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Uses phone.csv file to fill Phone model with content.'

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug = '-'.join(phone['name'].lower().split())
            phone.update({'slug': slug})
            Phone.objects.create(**phone)
