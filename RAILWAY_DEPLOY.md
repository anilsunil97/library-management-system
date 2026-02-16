# Deploy to Railway (Recommended)

Railway is a better option for Django applications than Vercel because it provides:
- Persistent PostgreSQL database
- No serverless limitations
- Easy deployment from GitHub
- Free tier available

## Prerequisites

1. Create a Railway account at https://railway.app
2. Push your code to GitHub

## Deployment Steps

### 1. Prepare Your Project

Add these files (already included):

**requirements.txt**
```
Django>=5.0,<6.0
psycopg2-binary
gunicorn
whitenoise
```

**Procfile** (create this):
```
web: gunicorn library_system.wsgi --log-file -
```

**runtime.txt** (create this):
```
python-3.12.0
```

### 2. Update settings.py for Railway

Add to settings.py:

```python
import dj_database_url

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# WhiteNoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 3. Deploy on Railway

1. Go to https://railway.app/dashboard
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will auto-detect Django

### 4. Add PostgreSQL Database

1. In your Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically set DATABASE_URL

### 5. Set Environment Variables

In Railway dashboard, add:
- `SECRET_KEY`: Your Django secret key
- `DEBUG`: False
- `ALLOWED_HOSTS`: your-app.railway.app

### 6. Run Migrations

In Railway dashboard:
1. Go to your service
2. Click "Settings" → "Deploy"
3. Add custom start command:
```bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn library_system.wsgi
```

Or use Railway CLI:
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

### 7. Access Your App

Your app will be available at: `https://your-app.railway.app`

## Benefits of Railway

✅ Persistent database (PostgreSQL)
✅ No cold starts
✅ Easy scaling
✅ Automatic HTTPS
✅ GitHub integration
✅ Environment variables management
✅ Free tier: $5 credit/month

## Cost

- Free tier: $5 credit/month (enough for small projects)
- Hobby plan: $5/month
- Pro plan: $20/month

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
