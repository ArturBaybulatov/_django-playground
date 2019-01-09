import url_filter.filtersets as filters

from . import models


class Note(filters.ModelFilterSet):
    class Meta:
        model = models.Note


class Tag(filters.ModelFilterSet):
    class Meta:
        model = models.Tag


class Synonym(filters.ModelFilterSet):
    class Meta:
        model = models.Synonym
