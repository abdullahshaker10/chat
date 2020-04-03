from django.views.generic import View, DetailView, ListView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import generics

from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .models import CustomUser
from .serializers import UserSerializer


class SignUpView(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class LoginView(auth_views.LoginView):
    template_name = 'login.html'


class Home(ListView):
    template_name = "index.html"
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(is_staff=False)


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        displayname = self.kwargs['username']
        return CustomUser.objects.filter(display_name=displayname)
