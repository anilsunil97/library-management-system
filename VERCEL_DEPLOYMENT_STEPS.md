# 🚀 Vercel Deployment - Step by Step Guide

## ⚠️ Important Notice

**Vercel Limitations for Django:**
- SQLite database will reset on each deployment
- Not recommended for production use
- Better for testing/demo purposes only
- For production, use Railway or Render (see RAILWAY_DEPLOY.md)

## 📋 Prerequisites

1. ✅ Vercel CLI installed (already done)
2. ✅ Vercel account (create at https://vercel.com)
3. ✅ All files configured (already done)

## 🔧 Deployment Steps

### Step 1: Login to Vercel

Open your terminal and run:

```bash
vercel login
```

- A browser window will open
- Login with your Vercel account (GitHub, GitLab, or Email)
- Return to terminal after successful login

### Step 2: Deploy to Vercel

Run the deployment command:

```bash
vercel
```

You'll be asked several questions:

**Question 1:** "Set up and deploy?"
- Answer: `Y` (Yes)

**Question 2:** "Which scope?"
- Select your Vercel account/team

**Question 3:** "Link to existing project?"
- Answer: `N` (No, create new project)

**Question 4:** "What's your project's name?"
- Enter: `library-management-system` (or your preferred name)

**Question 5:** "In which directory is your code located?"
- Answer: `./` (current directory)

**Question 6:** "Want to override the settings?"
- Answer: `N` (No, use detected settings)

Vercel will now:
- Upload your files
- Build the project
- Deploy to a preview URL

### Step 3: Deploy to Production

After successful preview deployment, deploy to production:

```bash
vercel --prod
```

This creates your production deployment.

### Step 4: Set Environment Variables

Go to your Vercel dashboard:

1. Visit: https://vercel.com/dashboard
2. Select your project
3. Go to "Settings" → "Environment Variables"
4. Add these variables:

```
SECRET_KEY = your-secret-key-here
DEBUG = False
```

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Redeploy with Environment Variables

After adding environment variables:

```bash
vercel --prod
```

## 🎉 Your App is Live!

Your application will be available at:
- Production: `https://your-project-name.vercel.app`
- Preview: `https://your-project-name-hash.vercel.app`

## ⚠️ Post-Deployment Limitations

### Database Resets
- SQLite database resets on each deployment
- You'll need to recreate admin and data after each deploy
- This is a Vercel limitation for Django apps

### What This Means:
- ❌ User registrations won't persist
- ❌ Borrowed books data will be lost
- ❌ Admin accounts need recreation
- ❌ Not suitable for production

## 🔄 After Each Deployment

Since the database resets, you need to:

1. **Create Superuser** (via Vercel CLI):
```bash
vercel exec -- python manage.py createsuperuser
```

2. **Or use Django Admin:**
- Visit: `https://your-app.vercel.app/admin/`
- You won't be able to login (no users exist)

## 💡 Better Alternatives

### For Production Use:

**Railway (Recommended):**
- Persistent PostgreSQL database
- No data loss
- Easy deployment
- See: RAILWAY_DEPLOY.md

**Render:**
- Free tier with PostgreSQL
- Persistent data
- See: QUICK_DEPLOY.md

## 🛠️ Troubleshooting

### Issue: Build Failed
**Solution:**
- Check `vercel logs`
- Ensure all files are committed
- Check requirements.txt

### Issue: 500 Internal Server Error
**Solution:**
- Check Vercel logs: `vercel logs`
- Verify environment variables
- Check ALLOWED_HOSTS in settings.py

### Issue: Static Files Not Loading
**Solution:**
- Run: `python manage.py collectstatic`
- Redeploy: `vercel --prod`

### Issue: Database Empty
**Solution:**
- This is expected on Vercel
- Database resets on each deploy
- Use Railway for persistent data

## 📊 Vercel Dashboard

Access your dashboard at: https://vercel.com/dashboard

From there you can:
- View deployments
- Check logs
- Manage environment variables
- Configure domains
- View analytics

## 🔗 Custom Domain (Optional)

1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions
4. Wait for DNS propagation

## 📝 Deployment Commands Reference

```bash
# Login to Vercel
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Remove deployment
vercel rm [deployment-url]

# Open project in browser
vercel open
```

## ⚡ Quick Deploy Script

Use the provided script:

**Windows:**
```bash
deploy.bat
```

**Linux/Mac:**
```bash
chmod +x deploy.sh
./deploy.sh
```

## 🎯 Summary

### What Works on Vercel:
✅ Application runs
✅ UI works perfectly
✅ Login/logout functionality
✅ Static files served
✅ Fast deployment

### What Doesn't Work:
❌ Persistent database
❌ User data retention
❌ File uploads
❌ Long-term data storage

## 🚀 Recommended Workflow

**For Testing/Demo:**
1. Deploy to Vercel
2. Share the URL
3. Demo the features
4. Accept data loss on redeploy

**For Production:**
1. Use Railway or Render
2. Get persistent PostgreSQL
3. Keep user data safe
4. See RAILWAY_DEPLOY.md

## 📞 Support

- Vercel Docs: https://vercel.com/docs
- Vercel Support: https://vercel.com/support
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

---

## ✅ Deployment Checklist

Before deploying:
- [ ] Vercel CLI installed
- [ ] Logged into Vercel
- [ ] All files committed
- [ ] Environment variables ready
- [ ] Understand database limitations

After deploying:
- [ ] App accessible via URL
- [ ] Static files loading
- [ ] Can access login page
- [ ] Understand data won't persist

---

**Ready to deploy?** Run `vercel` in your terminal!

**Need persistent data?** Check out RAILWAY_DEPLOY.md instead! 🚂
