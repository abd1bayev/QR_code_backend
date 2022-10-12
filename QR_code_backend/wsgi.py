# QR_code_backend/wsgi,py

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QR_code_backend.settings')

application = get_wsgi_application()
