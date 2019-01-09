from django.contrib.auth import get_user_model
import rest_framework_filters as filters

from . import models


class Note(filters.FilterSet):
    id = filters.AllLookupsFilter()
    name = filters.AllLookupsFilter()
    private = filters.AllLookupsFilter()
    share_count = filters.AllLookupsFilter()
    category = filters.RelatedFilter('base.filters.Category', queryset=models.Category.objects.all())

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',
            'category',
        )


class Category(filters.FilterSet):
    id = filters.AllLookupsFilter()
    name = filters.AllLookupsFilter()
    notes = filters.RelatedFilter('base.filters.Note', queryset=models.Note.objects.all())

    class Meta:
        model = models.Category

        fields = (
            'id',
            'name',
            'notes',
        )
