#!/usr/bin/env bash
set -e

gunicorn -w $WORKERS  -b 0.0.0.0:8000 $FLASK_APP