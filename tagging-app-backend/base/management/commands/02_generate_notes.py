from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating notes...')
        print('---------------------------------------')

        tags = tuple(models.Tag.objects.all())

        for i in range(0, 100):
            note = models.Note.objects.create(name='Note-%s' % (i + 1))
            note.tags.set(random.sample(tags, random.randint(5, 20)))

        print('---------------------------------------')
        print('Done generating notes...')
        print('---------------------------------------')
