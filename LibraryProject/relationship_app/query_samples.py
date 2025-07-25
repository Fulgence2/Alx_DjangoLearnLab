import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'relationship_app.settings'
django.setup()

from 