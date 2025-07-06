#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn Blogify.wsgi:application --bind 0.0.0.0:$PORT
