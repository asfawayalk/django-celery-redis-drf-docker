#!/bin/bash

set -e

function run() {
    python manage.py "$@"
}

run makemigrations --merge  --no-input --traceback
run migrate  --no-input --traceback
run runserver 0.0.0.0:8000
