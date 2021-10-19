"""
ASGI config for Proyecto3Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os #permite acceder a ciertas variables del sistema

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto3Django.settings')

application = get_asgi_application()
