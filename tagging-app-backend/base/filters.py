from django.contrib.auth import get_user_model
import rest_framework_filters as filters

from . import models


class Note(filters.FilterSet):
    id = filters.AllLookupsFilter()
    name = filters.AllLookupsFilter()

    tags = filters.RelatedFilter('base.filters.Tag', queryset=models.Tag.objects.all())

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',

            'tags',
        )


class Tag(filters.FilterSet):
    id = filters.AllLookupsFilter()
    name = filters.AllLookupsFilter()
    type = filters.AllLookupsFilter()
    level = filters.AllLookupsFilter()
    lft = filters.AllLookupsFilter()
    rght = filters.AllLookupsFilter()
    tree_id = filters.AllLookupsFilter()

    parent = filters.RelatedFilter('base.filters.Tag', queryset=models.Tag.objects.all())
    children = filters.RelatedFilter('base.filters.Tag', queryset=models.Tag.objects.all())
    notes = filters.RelatedFilter('base.filters.Note', queryset=models.Note.objects.all())

    class Meta:
        model = models.Tag

        fields = (
            'id',
            'name',
            'type',
            'level',
            'lft',
            'rght',
            'tree_id',

            'parent',
            'children',
            'notes',
        )
