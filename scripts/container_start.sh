#!/bin/sh
set -eu

PORT="${PORT:-8000}"
WEB_CONCURRENCY="${WEB_CONCURRENCY:-2}"
DB_PATH="${YTENX_DB_PATH:-/app/ytenx/ytenx.sqlite}"

echo "Starting ytenx container"
python --version
python -m django --version
gunicorn --version

if [ ! -s "$DB_PATH" ]; then
  echo "SQLite database is missing or empty: $DB_PATH" >&2
  exit 1
fi

python manage.py check

exec gunicorn ytenx.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "$WEB_CONCURRENCY" \
  --access-logfile - \
  --error-logfile -
