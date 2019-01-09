from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating products...')
        print('---------------------------------------')

        regions = tuple(models.Region.objects.exclude(level=0).all())
        categories = tuple(models.Category.objects.exclude(level=0).all())

        products = []

        for i in range(0, 1000):
            products.append(models.Product(
                name='Product-%s' % (i + 1),
                region=random.choice(regions),
            ))

        models.Product.objects.bulk_create(products)

        products = models.Product.objects.all()

        for product in products:
            product.categories = random.sample(categories, random.randint(1, 5))

        print('---------------------------------------')
        print('Done generating products...')
        print('---------------------------------------')
