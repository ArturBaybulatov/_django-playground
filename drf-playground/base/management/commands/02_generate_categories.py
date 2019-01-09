from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating categories...')
        print('---------------------------------------')

        categories = []

        for i in range(1, 11):
            categories.append(models.Category(name='Category-%s' % i))

        models.Category.objects.bulk_create(categories)

        print('---------------------------------------')
        print('Done generating categories...')
        print('---------------------------------------')
