from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint, pformat

from . import forms


class HomeView(View):
    template_name = 'base/home.html'
    form_class = forms.TestForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request, prefix='form_1')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request, prefix='form_1')

        if form.is_valid():
            messages.info(request, 'Form valid')

        pprint(form.cleaned_data) # Debug

        return render(request, self.template_name, {'form': form})


# import code; code.interact(local=dict(globals(), **locals()))
