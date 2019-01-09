from django.core.management import BaseCommand

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating categories...')
        print('---------------------------------------')

        categories = []

        for i in range(0, 10):
            categories.append(models.Category(name='Category-%s' % (i + 1)))

        models.Category.objects.bulk_create(categories)

        print('---------------------------------------')
        print('Done generating categories...')
        print('---------------------------------------')
