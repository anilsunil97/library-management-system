#!/bin/bash

# Exit on error
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
# Set environment variable to skip database checks
export DJANGO_SETTINGS_MODULE=library_system.settings
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
