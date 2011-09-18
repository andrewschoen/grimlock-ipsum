import sys
import os

os.environ["CELERY_LOADER"] = "django"
project_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0]
sys.path.append(project_path)
sys.path.append(project_path + '/grimlock_ipsum/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'grimlock_ipsum.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
