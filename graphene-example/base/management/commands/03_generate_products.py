from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating products...')
        print('---------------------------------------')

        for i in range(0, 100):
            product = models.Product.objects.create(
                name='Product-%s' % (i + 1),

                quantity=random.choice((
                    random.randrange(0, 10),
                    random.randrange(10, 100),
                    random.randrange(100, 1000),
                )),

                brand=models.Brand.objects.order_by('?').first(),
            )

            product.categories = models.Category.objects.order_by('?')[:random.randint(1, 3)]

        print('---------------------------------------')
        print('Done generating products...')
        print('---------------------------------------')
