# Check Vercel Environment Variables

## The Problem

You ran migrations successfully, but Vercel is still showing the error. This means:

**Vercel is NOT using the same database you just migrated!**

## Solution: Verify DATABASE_URL in Vercel

### Step 1: Check Vercel Environment Variables

1. Go to: https://vercel.com/dashboard
2. Open your project: `library-management-system`
3. Click **Settings** (top menu)
4. Click **Environment Variables** (left sidebar)
5. Look for `DATABASE_URL`

### Step 2: Verify the Value

Click the eye icon next to `DATABASE_URL` to reveal it.

**It MUST be EXACTLY:**
```
postgresql://neondb_owner:npg_TbC02uwSjnDB@ep-autumn-salad-aibea208-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require
```

### Step 3: Check Which Environments Are Selected

Make sure ALL THREE are checked:
- ✅ Production
- ✅ Preview
- ✅ Development

### Step 4: If DATABASE_URL is Missing or Wrong

1. Click **Add New** (or Edit if it exists)
2. **Key**: `DATABASE_URL`
3. **Value**: 
   ```
   postgresql://neondb_owner:npg_TbC02uwSjnDB@ep-autumn-salad-aibea208-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require
   ```
4. **Environments**: Check ALL boxes
5. Click **Save**

### Step 5: Remove Conflicting Variables

If you see any of these, they might be conflicting:
- `POSTGRES_URL`
- `POSTGRES_PRISMA_URL`
- `DATABASE_URL_UNPOOLED`

**Either:**
- Delete them, OR
- Make sure `DATABASE_URL` has the correct Neon connection string

### Step 6: Redeploy

After saving the environment variable:

1. Go to **Deployments** tab
2. Click the three dots (...) on the latest deployment
3. Click **Redeploy**
4. Wait for deployment to complete (1-2 minutes)

### Step 7: Check Deployment Logs

After redeployment:

1. Click on the deployment
2. Click **View Function Logs**
3. Look for the line that says:
   - ✅ `✓ Using PostgreSQL database from DATABASE_URL`
   - ❌ `⚠️ Using SQLite database (not suitable for Vercel!)`

If you see the SQLite message, DATABASE_URL is NOT being picked up!

## Common Issues

### Issue 1: Using Vercel Postgres Instead of Neon

If you created a Vercel Postgres database, it uses different variable names:
- `POSTGRES_URL` (Vercel's name)
- `DATABASE_URL` (Django's expected name)

**Fix**: Copy the value from `POSTGRES_URL` and create a new variable `DATABASE_URL` with the same value.

### Issue 2: Environment Not Selected

If you only checked "Production" but not "Preview", preview deployments won't work.

**Fix**: Edit the variable and check ALL environments.

### Issue 3: Typo in Connection String

Even a single character wrong will cause issues.

**Fix**: Copy-paste carefully, don't type it manually.

### Issue 4: Channel Binding Issue

If your connection string has `channel_binding=require`, remove it:

**Change from:**
```
postgresql://...?sslmode=require&channel_binding=require
```

**To:**
```
postgresql://...?sslmode=require
```

## Quick Verification Command

You can check what Vercel sees by adding a test endpoint. But first, just verify the environment variable is correct!

## After Fixing

1. Save the correct `DATABASE_URL`
2. Redeploy
3. Test: https://library-management-system-taupe-tau.vercel.app/register/

The error should be gone!
