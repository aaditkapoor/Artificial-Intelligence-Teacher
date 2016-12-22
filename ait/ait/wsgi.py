"""
WSGI config for ait project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ait.settings")

application = get_wsgi_application()


development_flag = False


if development_flag:
	from django.core.wsgi import get_wsgi_application
	from whitenoise.django import DjangoWhiteNoise

	application = get_wsgi_application()
	application = DjangoWhiteNoise(application)

else:
	application = get_wsgi_application()
