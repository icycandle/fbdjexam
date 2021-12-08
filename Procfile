web: gunicorn fbdjexam.wsgi
worker: celery -A fbdjexam.celery worker -B --loglevel=info
