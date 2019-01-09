from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint, pformat


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProtectedView(LoginRequiredMixin, View):
    template_name = 'base/protected.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(prefix='register')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, prefix='register')

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, 'Registration successful')
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})


# import code; code.interact(local=dict(globals(), **locals()))
