from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
import random

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating users...')
        print('---------------------------------------')

        for i in range(2, 11):
            get_user_model().objects.create_user('user-%s' % i, 'user-%s@example.com' % i, '123')

        print('---------------------------------------')
        print('Done generating users...')
        print('---------------------------------------')
