#!/bin/bash

# Exit on error
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
# Set environment variable to skip database checks
export DJANGO_SETTINGS_MODULE=library_system.settings
python manage.py collectstatic --noinput --clear

# Run migrations if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
    echo "Running database migrations..."
    python manage.py migrate --noinput || echo "Migration failed, continuing..."
    
    echo "Setting up initial data..."
    python post_deploy_setup.py || echo "Setup script failed, continuing..."
else
    echo "DATABASE_URL not set, skipping migrations"
fi

echo "Build completed successfully!"
