from django.urls import path
from .views import SignUpView, Home ,LoginView,LogoutView

urlpatterns = [
    path('', SignUpView.as_view(), name='register'),
    path('index/', Home.as_view(), name='index'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
