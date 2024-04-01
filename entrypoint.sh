#!/usr/bin/env bash
set -e
flask db upgrade
gunicorn -w $WORKERS  -b 0.0.0.0:$FLASK_RUN_PORT $FLASK_APP
