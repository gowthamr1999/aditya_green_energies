#!/usr/bin/env bash
set -euo pipefail

# Usage examples:
# ./startup.sh
# PORT=8000 BACKUP_DB=backups/prod.sqlite3 ./startup.sh
# FIXTURE_FILE=backups/data.json ./startup.sh

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

DB_FILE="${DB_FILE:-db.sqlite3}"
BACKUP_DB="${BACKUP_DB:-backups/db.sqlite3}"
FIXTURE_FILE="${FIXTURE_FILE:-backups/data.json}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
APP_MODULE="${APP_MODULE:-aditya.wsgi:application}"
RUN_SEED="${RUN_SEED:-false}"

PYTHON_BIN="${PYTHON_BIN:-python}"
if [[ -x "$PROJECT_ROOT/venv/bin/python" ]]; then
  PYTHON_BIN="$PROJECT_ROOT/venv/bin/python"
fi

echo "Using Python: $PYTHON_BIN"

# Ensure DB exists by restoring from backup when possible.
if [[ ! -f "$DB_FILE" ]]; then
  echo "Database not found: $DB_FILE"

  if [[ -f "$BACKUP_DB" ]]; then
    echo "Restoring SQLite DB from backup: $BACKUP_DB"
    cp "$BACKUP_DB" "$DB_FILE"
  else
    echo "No SQLite backup found at $BACKUP_DB"
    echo "Creating schema with migrations"
    "$PYTHON_BIN" manage.py migrate --noinput

    if [[ -f "$FIXTURE_FILE" ]]; then
      echo "Loading fixture: $FIXTURE_FILE"
      "$PYTHON_BIN" manage.py loaddata "$FIXTURE_FILE"
    else
      echo "No fixture file found at $FIXTURE_FILE; continuing with empty DB"
    fi
  fi
else
  echo "Database already exists: $DB_FILE"
fi

# Always apply migrations to keep schema up to date.
"$PYTHON_BIN" manage.py migrate --noinput

if [[ "$RUN_SEED" == "true" ]]; then
  echo "Running database seed command"
  "$PYTHON_BIN" manage.py seed_data
fi

# Optional static collection. Skip errors in case STATIC_ROOT is not configured.
"$PYTHON_BIN" manage.py collectstatic --noinput || true

if "$PYTHON_BIN" -m pip show gunicorn >/dev/null 2>&1; then
  echo "Starting with Gunicorn on ${HOST}:${PORT}"
  exec "$PYTHON_BIN" -m gunicorn "$APP_MODULE" --bind "${HOST}:${PORT}"
else
  echo "Gunicorn not installed, starting Django development server on ${HOST}:${PORT}"
  exec "$PYTHON_BIN" manage.py runserver "${HOST}:${PORT}"
fi
