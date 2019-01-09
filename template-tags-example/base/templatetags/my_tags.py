from django import template
from django.utils.safestring import mark_safe
from pprint import pprint, pformat
import json
import os


register = template.Library()


@register.filter
def inspect(obj):
    #return pformat(obj.__dict__)
    return pformat(obj) # Tmp


@register.simple_tag
def interact(**kwargs):
    import code; code.interact(local=dict(kwargs, **dict(globals(), **locals())))


@register.filter('int')
def to_int(val):
    return int(val)


@register.filter('str')
def to_str(val):
    return str(val)


@register.filter('range')
def to_range(num):
    return range(num)


@register.filter('list')
def to_list(val):
    return list(val)


@register.filter('repr')
def to_repr(val):
    return repr(val)


@register.filter('json')
def to_json(val):
    return mark_safe(repr(json.dumps(val)))


@register.filter
def class_name(val):
    return type(val).__name__


@register.filter
def get(dic, key):
    if isinstance(dic, dict):
        return dic.get(key)


# import code; code.interact(local=dict(globals(), **locals()))
