from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View


class HomeView(View):
    context = {'x': 5}
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        self.context = {'x': 8}
        return render(request, self.template_name, self.context)


class HelloView(LoginRequiredMixin, View):
    context = {'x': 5}
    login_url = reverse_lazy('common:login')
    redirect_to = reverse_lazy('common:home')
    template_name = 'hello.html'
    
    def post(self, request, *args, **kwargs):
        messages.info(request, 'Hello right back at cha')
        
        next = request.POST.get('next')
        
        if next:
            self.redirect_to = next
        
        return redirect(self.redirect_to)


class RedirectedView(View):
    context = {}
    template_name = 'redirected.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class LoginView(View):
    context = {}
    redirect_to = reverse_lazy('common:home')
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                messages.info(request, "You've been logged in")
                next = request.POST.get('next')
                
                if next:
                    self.redirect_to = next
            else:
                messages.info(request, "Log-in failed")
        
        return redirect(self.redirect_to)


class LogoutView(View):
    redirect_to = reverse_lazy('common:home')
    
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "You've been logged out")
        next = request.POST.get('next')
        
        if next:
            self.redirect_to = next
        
        return redirect(self.redirect_to)


# import code; code.interact(local=dict(globals(), **locals()))
