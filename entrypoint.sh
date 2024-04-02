#!/usr/bin/env bash
set -e
sleep 5

flask db upgrade
# wait for the database to be ready
gunicorn -w $WORKERS  -b 0.0.0.0:$FLASK_RUN_PORT $FLASK_APP
