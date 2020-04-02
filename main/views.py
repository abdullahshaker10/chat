from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


class SignUpView(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class LoginView(auth_views.LoginView):
    template_name = 'login.html'


class Home(TemplateView):
    template_name = "index.html"


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'
