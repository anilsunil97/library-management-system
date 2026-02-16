# Deployment Guide for Vercel

## Important Notes

⚠️ **Vercel Limitations for Django:**
- Vercel is designed for serverless/static sites, not traditional Django apps
- SQLite database will reset on each deployment (use PostgreSQL for production)
- File uploads won't persist (use cloud storage like AWS S3)
- Better alternatives: Railway, Render, PythonAnywhere, or DigitalOcean

## Prerequisites

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Create a Vercel account at https://vercel.com

## Deployment Steps

### Option 1: Deploy via Vercel CLI

1. Login to Vercel:
```bash
vercel login
```

2. Deploy the project:
```bash
vercel
```

3. Follow the prompts:
   - Set up and deploy? Yes
   - Which scope? Select your account
   - Link to existing project? No
   - Project name? library-management-system (or your choice)
   - Directory? ./
   - Override settings? No

4. For production deployment:
```bash
vercel --prod
```

### Option 2: Deploy via GitHub

1. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/library-system.git
git push -u origin main
```

2. Go to https://vercel.com/dashboard
3. Click "Add New Project"
4. Import your GitHub repository
5. Vercel will auto-detect settings
6. Click "Deploy"

## Environment Variables

Set these in Vercel Dashboard (Settings → Environment Variables):

- `SECRET_KEY`: Your Django secret key
- `DEBUG`: Set to `False` for production

## Post-Deployment Setup

⚠️ **Important:** Since SQLite resets on Vercel, you need to:

1. Run migrations (will reset on each deploy):
```bash
vercel exec -- python manage.py migrate
```

2. Create superuser (will reset on each deploy):
```bash
vercel exec -- python manage.py createsuperuser
```

## Recommended Production Setup

For a production-ready deployment, consider these alternatives:

### 1. Railway (Recommended)
- Supports Django natively
- Persistent PostgreSQL database
- Easy deployment
- Free tier available
- Visit: https://railway.app

### 2. Render
- Free tier with PostgreSQL
- Automatic deployments from Git
- Visit: https://render.com

### 3. PythonAnywhere
- Django-specific hosting
- Free tier available
- Visit: https://www.pythonanywhere.com

### 4. DigitalOcean App Platform
- Full Django support
- Managed databases
- Visit: https://www.digitalocean.com/products/app-platform

## Database Migration for Production

To use PostgreSQL instead of SQLite:

1. Install psycopg2:
```bash
pip install psycopg2-binary
```

2. Update requirements.txt:
```
Django>=5.0,<6.0
psycopg2-binary
```

3. Update settings.py:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

4. Set DATABASE_URL environment variable in Vercel

## Troubleshooting

### Static files not loading
- Run: `python manage.py collectstatic`
- Check STATIC_ROOT in settings.py

### Database resets on each deploy
- This is expected with SQLite on Vercel
- Use PostgreSQL for persistent data

### 500 Internal Server Error
- Check Vercel logs: `vercel logs`
- Ensure DEBUG=False in production
- Check ALLOWED_HOSTS includes your domain

## Support

For issues specific to this deployment, check:
- Vercel Documentation: https://vercel.com/docs
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
