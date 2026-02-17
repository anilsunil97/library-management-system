# Fix Vercel Database Issue

## Problem
Vercel is a **serverless platform** with a **read-only filesystem**. SQLite databases don't work on Vercel because:
- SQLite needs to write to a file
- Vercel's filesystem is read-only
- Each request runs in a new isolated environment

## Solution: Use PostgreSQL

### Option 1: Vercel Postgres (Recommended)

1. **Go to your Vercel project dashboard**
   - https://vercel.com/dashboard

2. **Add Vercel Postgres**
   - Click on your project
   - Go to "Storage" tab
   - Click "Create Database"
   - Select "Postgres"
   - Choose a name (e.g., "library-db")
   - Click "Create"

3. **Connect to your project**
   - Vercel will automatically add environment variables:
     - `POSTGRES_URL`
     - `POSTGRES_PRISMA_URL`
     - `POSTGRES_URL_NON_POOLING`

4. **Redeploy**
   - Your app will automatically use PostgreSQL
   - Run migrations on first deploy

### Option 2: Neon (Free PostgreSQL)

1. **Create account at https://neon.tech**

2. **Create a new project**
   - Name: library-management
   - Region: Choose closest to you

3. **Copy connection string**
   - Format: `postgresql://user:password@host/database?sslmode=require`

4. **Add to Vercel environment variables**
   - Go to Vercel project settings
   - Environment Variables
   - Add: `DATABASE_URL` = your connection string

5. **Redeploy**

### Option 3: Supabase (Free PostgreSQL)

1. **Create account at https://supabase.com**

2. **Create new project**
   - Name: library-management
   - Database password: (save this!)

3. **Get connection string**
   - Go to Project Settings > Database
   - Copy "Connection string" (URI format)
   - Replace `[YOUR-PASSWORD]` with your actual password

4. **Add to Vercel**
   - Environment Variables
   - Add: `DATABASE_URL` = connection string

5. **Redeploy**

## After Setting Up Database

### Run Migrations on Vercel

Create `post_deploy_setup.py` (already exists) and it will run automatically.

Or manually via Vercel CLI:
```bash
vercel env pull
python manage.py migrate
```

### Create Admin User

You'll need to create an admin user. Add this to your deployment:

1. Go to Vercel project settings
2. Add environment variable:
   - `DJANGO_SUPERUSER_USERNAME` = admin
   - `DJANGO_SUPERUSER_EMAIL` = admin@example.com
   - `DJANGO_SUPERUSER_PASSWORD` = your-secure-password

3. Update `post_deploy_setup.py` to create superuser

## Quick Fix (Use Neon - Fastest)

1. Go to https://neon.tech and sign up
2. Create project, copy connection string
3. Go to Vercel project > Settings > Environment Variables
4. Add `DATABASE_URL` with your Neon connection string
5. Redeploy from Vercel dashboard

Your settings.py already supports this - it will automatically use `DATABASE_URL` if available!

## Current Settings Support

Your `library_system/settings.py` already has:
```python
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Production: Use PostgreSQL
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Development: Use SQLite
    DATABASES = {...}
```

So you just need to add the `DATABASE_URL` environment variable in Vercel!

## Recommended: Neon (Easiest & Free)

1. **Sign up**: https://neon.tech
2. **Create project**: Click "Create Project"
3. **Copy connection string**: Shows immediately after creation
4. **Add to Vercel**: 
   - Settings > Environment Variables
   - Name: `DATABASE_URL`
   - Value: (paste connection string)
5. **Redeploy**: Vercel dashboard > Deployments > Redeploy

Done! Your app will now use PostgreSQL instead of SQLite.
