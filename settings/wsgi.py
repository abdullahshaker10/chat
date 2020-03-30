"""
<<<<<<< HEAD
WSGI config for settings project.
=======
WSGI config for chatapp project.
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf

application = get_wsgi_application()
