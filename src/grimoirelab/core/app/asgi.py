"""ASGI config for grimoirelab project"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grimoirelab.core.config.settings')

application = get_asgi_application()
