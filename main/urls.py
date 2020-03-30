from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name='register'),
    path('index/', TemplateView.as_view(template_name="index.html"), name='index'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
