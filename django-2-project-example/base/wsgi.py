from django.core.wsgi import get_wsgi_application
from django.template.base import Variable
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
application = get_wsgi_application()


# Patch template Variable to output empty string for None values:

old_resolve_lookup = Variable._resolve_lookup

def new_resolve_lookup(self, *args, **kwargs):
    val = old_resolve_lookup(self, *args, **kwargs)
    return '' if val == None else val

Variable._resolve_lookup = new_resolve_lookup
