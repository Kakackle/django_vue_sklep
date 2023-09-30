#!/usr/bin/env bash
# exit on error
set -o errexit

# npm install
pip install -r requirements.txt
npm run build
python manage.py collectstatic --no-input
python manage.py migrate