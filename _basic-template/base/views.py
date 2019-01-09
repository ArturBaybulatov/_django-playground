from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint, pformat


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# import code; code.interact(local=dict(globals(), **locals()))
