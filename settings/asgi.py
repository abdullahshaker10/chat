"""
<<<<<<< HEAD
ASGI config for settings project.
=======
ASGI config for chatapp project.
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

application = get_asgi_application()
