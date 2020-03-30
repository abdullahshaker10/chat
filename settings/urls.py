<<<<<<< HEAD
"""chat URL Configuration
=======
"""chatapp URL Configuration

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),
]
=======
urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
