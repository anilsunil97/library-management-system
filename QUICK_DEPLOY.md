# Quick Deployment Guide

## 🚀 Fastest Way to Deploy

### Option 1: Railway (Recommended - 5 minutes)

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/library-system.git
git push -u origin main
```

2. **Deploy on Railway:**
   - Go to https://railway.app
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Add PostgreSQL database (click "New" → "Database" → "PostgreSQL")
   - Set environment variables:
     - `SECRET_KEY`: (generate one)
     - `DEBUG`: False
   - Deploy!

3. **Run migrations:**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link project
railway link

# Run migrations
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

✅ Done! Your app is live with a persistent database.

---

### Option 2: Vercel (Quick but Limited)

⚠️ **Warning:** Database resets on each deployment. Use for testing only.

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

---

### Option 3: Render (Free Tier)

1. Push to GitHub (same as Railway)
2. Go to https://render.com
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Settings:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn library_system.wsgi:application`
6. Add PostgreSQL database
7. Deploy!

---

## Environment Variables Needed

For all platforms, set these:

```
SECRET_KEY=your-secret-key-here-make-it-long-and-random
DEBUG=False
DATABASE_URL=postgresql://... (auto-set by Railway/Render)
```

## Generate Secret Key

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Post-Deployment Checklist

- [ ] Run migrations
- [ ] Create superuser
- [ ] Test login
- [ ] Test book borrowing
- [ ] Test fine calculation
- [ ] Add sample books

## Need Help?

- Railway: See [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)
- Vercel: See [DEPLOYMENT.md](DEPLOYMENT.md)
- Issues: Check application logs on your platform
