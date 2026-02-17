# Quick Fix for Vercel Database Error

## The Problem
❌ **SQLite doesn't work on Vercel** (serverless platform with read-only filesystem)

## The Solution (5 Minutes)

### Step 1: Get Free PostgreSQL Database

**Option A: Neon (Recommended - Easiest)**
1. Go to https://neon.tech
2. Click "Sign Up" (use GitHub login for fastest)
3. Click "Create Project"
4. Copy the connection string shown (starts with `postgresql://`)

**Option B: Vercel Postgres**
1. Go to https://vercel.com/dashboard
2. Open your project
3. Click "Storage" tab
4. Click "Create Database" > "Postgres"
5. Connection string will be auto-added

### Step 2: Add Database to Vercel

1. Go to your Vercel project: https://vercel.com/dashboard
2. Click on your project: `library-management-system`
3. Go to **Settings** > **Environment Variables**
4. Click **Add New**
   - **Name**: `DATABASE_URL`
   - **Value**: (paste your PostgreSQL connection string)
   - **Environment**: Select all (Production, Preview, Development)
5. Click **Save**

### Step 3: Redeploy

1. Go to **Deployments** tab
2. Click the three dots (...) on the latest deployment
3. Click **Redeploy**
4. Wait for deployment to complete

### Step 4: Run Migrations (One Time)

After deployment, you need to run migrations once. Two options:

**Option A: Using Vercel CLI (Recommended)**
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Link project
vercel link

# Pull environment variables
vercel env pull

# Run migrations
python manage.py migrate

# Create admin and sample data
python post_deploy_setup.py
```

**Option B: Add to requirements.txt and let it auto-run**
Your app is already configured to run migrations automatically on Vercel.

### Step 5: Test

Visit: https://library-management-system-taupe-tau.vercel.app/register/

Registration should now work! ✅

## What Changed

Your `settings.py` already supports this:
- If `DATABASE_URL` exists → Use PostgreSQL
- If not → Use SQLite (local development only)

## Connection String Format

Your connection string should look like:
```
postgresql://username:password@host:5432/database?sslmode=require
```

## Troubleshooting

### "relation does not exist" error
Run migrations:
```bash
vercel env pull
python manage.py migrate
```

### "no password supplied" error
Make sure your connection string includes the password:
```
postgresql://user:PASSWORD@host/db
```

### Still getting SQLite error
1. Check environment variable is saved in Vercel
2. Make sure you redeployed after adding it
3. Check deployment logs for errors

## Free Database Limits

- **Neon**: 10 GB storage, 100 hours compute/month
- **Vercel Postgres**: 256 MB storage, 60 hours compute/month
- **Supabase**: 500 MB storage, unlimited requests

All are free and more than enough for this project!

## Need Help?

1. Check Vercel deployment logs
2. Make sure `DATABASE_URL` is set in environment variables
3. Verify connection string format is correct
4. Ensure you redeployed after adding the variable
