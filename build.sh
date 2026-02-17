#!/bin/bash
# Vercel build script

echo "🔨 Building application..."

# Install dependencies
pip install -r requirements.txt

# Run migrations
echo "📦 Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run post-deployment setup (create admin, sample data)
echo "🚀 Running post-deployment setup..."
python post_deploy_setup.py || echo "⚠️  Post-deploy setup failed (might already be set up)"

echo "✅ Build complete!"
