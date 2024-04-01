#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

MAX_WAIT_SECONDS=60
SECONDS=0

postgres_ready() {
    python << END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${DJANGO_POSTGRES_DATABASE}",
        user="${DJANGO_POSTGRES_USER}",
        password="${DJANGO_POSTGRES_PASSWORD}",
        host="${DJANGO_POSTGRES_HOST}",
        port="${DJANGO_POSTGRES_PORT}",
    )
except OperationalError:
    sys.exit(-1)
END
}

until postgres_ready || [ $SECONDS -ge $MAX_WAIT_SECONDS ]; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 5
done

if [ $SECONDS -ge $MAX_WAIT_SECONDS ]; then
  >&2 echo "Timed out waiting for PostgreSQL"
  exit 1
fi

>&2 echo "PostgreSQL is available"

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
