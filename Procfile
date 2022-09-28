release: sh -c 'python manage.py migrate; find -L . -name "*.json" -exec python manage.py loaddata {} \;'
web: gunicorn project_django.wsgi --log-file -