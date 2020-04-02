from django.contrib.auth.decorators import login_required
from django.urls import path
from main import views

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('home/', login_required(views.Home.as_view()), name='home'),
    path('/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
