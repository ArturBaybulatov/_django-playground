from graphene import relay
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from . import models


class Product(DjangoObjectType):
    class Meta:
        model = models.Product

        filter_fields = {
            'id': ('exact',),
            'name': ('exact','iexact','icontains'),
            'quantity': ('exact','lt','lte','gt','gte','in','range'),
            'brand__luxury': ('exact',),
        }

        interfaces = (relay.Node,)


class Brand(DjangoObjectType):
    class Meta:
        model = models.Brand

        filter_fields = {
            'id': ('exact',),
            'name': ('exact','iexact','icontains'),
            'luxury': ('exact',),
            'products__quantity': ('exact','lt','lte','gt','gte','in','range'),
        }

        interfaces = (relay.Node,)


class Category(DjangoObjectType):
    class Meta:
        model = models.Category

        filter_fields = {
            'id': ('exact',),
            'name': ('exact','iexact','icontains'),
            'products__quantity': ('exact','lt','lte','gt','gte','in','range'),
        }

        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    product = relay.Node.Field(Product)
    brand = relay.Node.Field(Brand)
    category = relay.Node.Field(Category)

    products = DjangoFilterConnectionField(Product)
    #products = DjangoFilterConnectionField(Product, filterset_class=filters.Product) # Custom filterset
    brands = DjangoFilterConnectionField(Brand)
    categories = DjangoFilterConnectionField(Category)


schema = graphene.Schema(query=Query)
