# Vercel Environment Variables - Step by Step Guide

## Step 1: Go to Your Vercel Dashboard

1. Open: https://vercel.com
2. Click "Login" (top right)
3. You should see your projects

## Step 2: Open Your Project

1. Find your project: `library-management-system` (or similar name)
2. Click on it to open

## Step 3: Go to Settings

Look at the TOP of the page, you'll see tabs:
- Overview
- Deployments
- Analytics
- Logs
- **Settings** ← Click this one

## Step 4: Find Environment Variables

On the LEFT sidebar, you'll see:
- General
- Domains
- Git
- **Environment Variables** ← Click this one
- Functions
- etc.

## Step 5: Add New Variable

You should now see a page titled "Environment Variables"

1. Look for a button that says **"Add New"** or **"Add"** (usually top right)
2. Click it

## Step 6: Fill in the Form

You'll see a form with these fields:

**Field 1: Key (or Name)**
```
DATABASE_URL
```
Type exactly: `DATABASE_URL` (all caps, with underscore)

**Field 2: Value**
```
postgresql://username:password@host/database
```
Paste your PostgreSQL connection string from Neon here

**Field 3: Environment (Checkboxes)**

You'll see checkboxes for:
- [ ] Production
- [ ] Preview  
- [ ] Development

**Check ALL THREE boxes** ✓

## Step 7: Save

Click the **"Save"** button at the bottom

## Step 8: Verify It Was Added

After saving, you should see your new variable in the list:
```
DATABASE_URL    •••••••••••••    Production, Preview, Development
```

## Step 9: Redeploy

Now you need to redeploy for changes to take effect:

1. Click **"Deployments"** tab (top of page)
2. You'll see a list of deployments
3. Find the most recent one (top of list)
4. On the right side, click the **three dots (⋮)** or **(...)**
5. Click **"Redeploy"**
6. A popup appears, click **"Redeploy"** again to confirm
7. Wait 1-2 minutes for deployment to complete

## Alternative: Use Vercel's Built-in Postgres

If you don't want to use Neon, Vercel has its own database:

### Step 1: Go to Storage Tab
1. In your project, look for **"Storage"** tab (top menu)
2. Click it

### Step 2: Create Database
1. Click **"Create Database"** button
2. Select **"Postgres"**
3. Choose a name (e.g., `library-db`)
4. Select region (choose closest to you)
5. Click **"Create"**

### Step 3: Connect to Project
1. After creation, click **"Connect Project"**
2. Select your project from dropdown
3. Click **"Connect"**

### Step 4: Verify Environment Variables
1. Go back to Settings > Environment Variables
2. You should now see several variables automatically added:
   - `POSTGRES_URL`
   - `POSTGRES_PRISMA_URL`
   - `POSTGRES_URL_NON_POOLING`
   - etc.

### Step 5: Add DATABASE_URL
Even though Vercel added `POSTGRES_URL`, your Django app looks for `DATABASE_URL`:

1. Click **"Add New"**
2. Key: `DATABASE_URL`
3. Value: Copy the value from `POSTGRES_URL` (click the eye icon to reveal it)
4. Check all environments
5. Save

### Step 6: Redeploy
Same as before - go to Deployments and redeploy.

## Troubleshooting

### "I don't see Settings tab"
- Make sure you're viewing YOUR project (not someone else's)
- You need to be the owner or have admin access

### "I don't see Environment Variables in sidebar"
- Make sure you clicked "Settings" tab first
- Scroll down in the left sidebar

### "I don't see Add New button"
- You might not have permission
- Try refreshing the page
- Make sure you're logged in

### "Where do I get the PostgreSQL connection string?"

**Option 1: Neon (External)**
1. Go to https://neon.tech
2. Sign up / Login
3. Create new project
4. Connection string is shown immediately after creation
5. Format: `postgresql://user:pass@host.region.neon.tech/db?sslmode=require`

**Option 2: Vercel Postgres (Built-in)**
1. Use the "Storage" tab method above
2. Copy from `POSTGRES_URL` variable

## Still Stuck?

Take a screenshot of your Vercel project page and I can help identify where to click!

Common issues:
- Not logged into Vercel
- Viewing wrong project
- Don't have admin permissions
- Using old Vercel interface (try refreshing)
