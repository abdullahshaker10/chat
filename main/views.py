from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
