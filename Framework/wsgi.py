"""
WSGI config for Framework project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/Volumes/Data/nfs/zfs-student-4/users/2014_paris/rclanget/django/apps/django/django_projects/Framework')
os.environ.setdefault("PYTHON_EGG_CACHE", "/Volumes/Data/nfs/zfs-student-4/users/2014_paris/rclanget/django/apps/django/django_projects/Framework/egg_cache")

os.environ["DJANGO_SETTINGS_MODULE"] = "Framework.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
