"""
WSGI config for ad_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ad_service.settings")
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ui_app.settings")
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485

application = get_wsgi_application()