from . import serializers


def serialize_tree(item):
    item_dict = serializers.Tag(item).data
    item_dict['_children'] = tuple(map(serialize_tree, item.get_children()))
    return item_dict


# import code; code.interact(local=dict(globals(), **locals()))
