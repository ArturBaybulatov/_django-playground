from django.core.management import BaseCommand

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating regions...')
        print('---------------------------------------')

        depths = ('A','B','C','D')

        root = models.Region.objects.create(name='_root')

        for d1 in depths:
            x = models.Region.objects.create(name='Region-%s' % d1, parent=root)

            for d2 in depths:
                y = models.Region.objects.create(name='Region-%s-%s' % (d1, d2), parent=x)

                for d3 in depths:
                    models.Region.objects.create(name='Region-%s-%s-%s' % (d1, d2, d3), parent=y)

        print('---------------------------------------')
        print('Done generating regions...')
        print('---------------------------------------')
