from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating notes...')
        print('---------------------------------------')

        for i in range(1, 1001):
            note = models.Note.objects.create(
                name='Note-%s' % i,
                private=random.choice((True, False)),

                share_count=random.choice((
                    random.randrange(0, 10), # 0-9
                    random.randrange(10, 100), # 10-99
                    random.randrange(100, 1000), # 100-999
                )),

                category=models.Category.objects.order_by('?').first(),
                author=get_user_model().objects.order_by('?').first(),
            )

            note.categories = models.Category.objects.order_by('?')[:random.randint(1, 3)]

        print('---------------------------------------')
        print('Done generating notes...')
        print('---------------------------------------')
