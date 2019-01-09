from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating something...')
        print('---------------------------------------')
        
        ...
