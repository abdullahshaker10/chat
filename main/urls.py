from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from main import views
from main.views import UsersList

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    url('^users/(?P<username>.+)/$', UsersList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', login_required(views.Home.as_view()), name='home'),
    path('', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
