from django.core.management import BaseCommand
from mptt.templatetags.mptt_tags import cache_tree_children
from pprint import pprint
import json

from base import models, util


class Command(BaseCommand):
    def handle(self, *args, **options):
        serialized = util.serialize_tree(models.Tag.objects.root_nodes()[20])

        pprint(serialized)
        #print(json.dumps(serialized, indent=4))


# import code; code.interact(local=dict(globals(), **locals()))
