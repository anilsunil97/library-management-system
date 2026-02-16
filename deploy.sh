#!/bin/bash

echo "🚀 Library Management System - Deployment Script"
echo "================================================"
echo ""

# Check if vercel is installed
if ! command -v vercel &> /dev/null
then
    echo "❌ Vercel CLI is not installed."
    echo "📦 Install it with: npm install -g vercel"
    exit 1
fi

echo "✅ Vercel CLI found"
echo ""

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo ""
echo "🚀 Deploying to Vercel..."
echo ""

# Deploy
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "⚠️  Important Post-Deployment Steps:"
echo "1. Run migrations on Vercel"
echo "2. Create superuser account"
echo "3. Add sample data if needed"
echo ""
echo "📚 See DEPLOYMENT.md for detailed instructions"
