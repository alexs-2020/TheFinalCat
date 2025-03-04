web: gunicorn catSite.wsgi --log-file -

web: python3 manage.py migrate && gunicorn catSite.wsgi