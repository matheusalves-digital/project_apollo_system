#!/bin/sh

while ! nc -z postgres 5432; do
  echo "Aguardando o PostgreSQL iniciar..."
  sleep 1
done

python manage.py runserver 0.0.0.0:8000
