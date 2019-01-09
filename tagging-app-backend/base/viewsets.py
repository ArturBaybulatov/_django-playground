from rest_framework import viewsets

from . import models, serializers, filters_2


class Note(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.Note
    filter_class = filters_2.Note

    #def get_queryset(self):
    #    if self.request.user.is_authenticated():
    #        return self.request.user.notes.all()
    #
    #    return models.Note.objects.none()


class Tag(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filter_class = filters_2.Tag


class Synonym(viewsets.ModelViewSet):
    queryset = models.Synonym.objects.all()
    serializer_class = serializers.Synonym
    filter_class = filters_2.Synonym


# import code; code.interact(local=dict(globals(), **locals()))
