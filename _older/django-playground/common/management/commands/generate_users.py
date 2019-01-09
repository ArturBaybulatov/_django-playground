from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating users...')
        print('---------------------------------------')
        
        User.objects.create_superuser('admin', '', 123456)
        
        for i in range(1, 11):
            user = User()
            user.username = 'user-%s' % i
            user.set_password('123')
            user.save()
