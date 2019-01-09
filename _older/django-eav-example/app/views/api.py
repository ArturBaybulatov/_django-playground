from rest_framework import viewsets
from app import models, serializers, filters


class Category(viewsets.ModelViewSet):
  queryset = models.Category.objects.all()
  serializer_class = serializers.Category
  filter_class = filters.Category


class Advert(viewsets.ModelViewSet):
  queryset = models.Advert.objects.all()
  serializer_class = serializers.Advert
  filter_class = filters.Advert


class EavAttribute(viewsets.ModelViewSet):
  queryset = models.EavAttribute.objects.all()
  serializer_class = serializers.EavAttribute
  filter_class = filters.EavAttribute
