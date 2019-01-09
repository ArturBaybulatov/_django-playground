from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint, pformat

from . import models


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        region = models.Region.objects.filter(level__in=(1,2)).order_by('?').first()
        categories = tuple(models.Category.objects.filter(level__in=(1,2)).order_by('?')[:2])
        category1 = categories[0]
        category2 = categories[1]

        products = models.Product.objects\
            .filter(
                region__lft__gte=region.lft,
                region__rght__lte=region.rght,

                categories__lft__gte=category1.lft,
                categories__rght__lte=category1.rght,
            )\
            \
            .filter(
                categories__lft__gte=category2.lft,
                categories__rght__lte=category2.rght,
            )

        return render(request, self.template_name, {
            'region': region,
            'category1': category1,
            'category2': category2,
            'products': products,
        })


# import code; code.interact(local=dict(globals(), **locals()))
