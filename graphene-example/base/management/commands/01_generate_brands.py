from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating brands...')
        print('---------------------------------------')

        brands = []

        for i in range(0, 10):
            brands.append(models.Brand(
                name='Brand-%s' % (i + 1),
                luxury=random.choice((True, False)),
            ))

        models.Brand.objects.bulk_create(brands)

        print('---------------------------------------')
        print('Done generating brands...')
        print('---------------------------------------')
