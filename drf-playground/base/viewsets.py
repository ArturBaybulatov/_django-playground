from rest_framework import viewsets

from . import models, serializers, filters


class Note(viewsets.ModelViewSet):
    #queryset = models.Note.objects.none()
    queryset = models.Note.objects.all()
    serializer_class = serializers.Note
    filter_class = filters.Note

    #def get_queryset(self):
    #    if self.request.user.is_authenticated():
    #        return self.request.user.notes.all()
    #
    #    return models.Note.objects.none()


class Category(viewsets.ModelViewSet):
    #queryset = models.Category.objects.none()
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category
    filter_class = filters.Category

    #def get_queryset(self):
    #    if self.request.user.is_authenticated():
    #        return models.Category.objects.filter(notes__author=self.request.user).distinct()
    #
    #    return models.Category.objects.none()



# import code; code.interact(local=dict(globals(), **locals()))
