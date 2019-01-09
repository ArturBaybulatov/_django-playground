from django.core.management import BaseCommand

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating categories...')
        print('---------------------------------------')

        depths = ('A','B','C','D')

        root = models.Category.objects.create(name='_root')

        for d1 in depths:
            x = models.Category.objects.create(name='Category-%s' % d1, parent=root)

            for d2 in depths:
                y = models.Category.objects.create(name='Category-%s-%s' % (d1, d2), parent=x)

                for d3 in depths:
                    models.Category.objects.create(name='Category-%s-%s-%s' % (d1, d2, d3), parent=y)

        print('---------------------------------------')
        print('Done generating categories...')
        print('---------------------------------------')
