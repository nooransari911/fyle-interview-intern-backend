#!/bin/bash

# to stop on first error
set -e

# Delete older .pyc files
# find . -type d \( -name env -o -name venv  \) -prune -false -o -name "*.pyc" -exec rm -rf {} \;

# Run required migrations
 export PYTHONPATH=/home/ansarimn/Downloads/fyle-interview-intern-backend/core/:/home/ansarimn/Downloads/fyle-interview-intern-backend/core/tests/:$PYTHONPATH
export PYTHONPATH=/home/ansarimn/Downloads/fyle-interview-intern-backend/:$PYTHONPATH
export FLASK_APP=core/server.py

# flask db init -d core/migrations/
# flask db migrate -m "Initial migration." -d core/migrations/
# flask db upgrade -d core/migrations/

# Run server
gunicorn -c gunicorn_config.py core.server:app

python3 ./core/tests/principals_test.py