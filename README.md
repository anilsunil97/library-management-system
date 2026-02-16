# Library Management System

A Django-based library management system with student registration, admin approval, and book management.

## 🚀 Quick Links

- **Want to Deploy NOW?** → [DEPLOY_NOW.md](DEPLOY_NOW.md) ⚡
- **Vercel Deployment** → [VERCEL_DEPLOYMENT_STEPS.md](VERCEL_DEPLOYMENT_STEPS.md)
- **Railway Deployment** → [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md) (Recommended)
- **Local Development** → See below
- **Deployment Comparison** → [DEPLOYMENT_COMPARISON.md](DEPLOYMENT_COMPARISON.md)

## Features

- Dual login system (separate student and admin login tabs)
- Student self-registration with roll number
- Admin approval system for new students
- Student login to view and borrow books
- Book search functionality (by title, author, or ISBN)
- Admin login to manage books, students, and approvals
- Book borrowing and returning system with 14-day limit
- Automatic fine calculation: ₹1 per day after 14 days
- Fine tracking and payment system
- Overdue book monitoring
- Admin panel for full CRUD operations
- Colorful and modern UI design

## Local Development Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create sample data (optional):
```bash
python setup_data.py
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Access the application at: http://127.0.0.1:8000/

## Deployment

Your app is ready to deploy! Choose your platform:

### 🥇 Railway (Recommended)
Best for Django with persistent PostgreSQL database.

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git push origin main

# 2. Deploy on railway.app
# - Connect GitHub repo
# - Add PostgreSQL database
# - Set environment variables
# - Deploy!

# 3. Run setup
railway run python manage.py migrate
railway run python post_deploy_setup.py
```

📖 **Detailed Guide:** [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)

### 🥈 Render
Free tier with PostgreSQL included.

```bash
# Push to GitHub, then deploy on render.com
```

### 🥉 Vercel (Testing Only)
⚠️ Database resets on each deployment.

```bash
npm install -g vercel
vercel --prod
```

📖 **All Deployment Options:** [DEPLOY_SUMMARY.md](DEPLOY_SUMMARY.md)

## Post-Deployment Setup

After deploying, run:

```bash
# Run migrations
python manage.py migrate

# Create initial data
python post_deploy_setup.py
```

This creates:
- Admin account (admin/admin123)
- Sample student (student1/student123)
- Sample books

## Login Credentials

### Admin
- Username: `admin`
- Password: `admin123`
- Access: Full admin panel at /admin/ and admin dashboard
- Can approve/reject student registrations

### Student
- Username: `student1`
- Password: `student123`
- Roll No: `ROLL001`
- Access: Student dashboard to borrow/return books

## New Student Registration

1. Go to http://127.0.0.1:8000/register/
2. Fill in the registration form with:
   - First Name & Last Name
   - Username & Email
   - Student ID & Roll Number
   - Phone Number
   - Password
3. Submit the form
4. Wait for admin approval
5. Once approved, login with your credentials

## Usage

### For Students:
- Register for a new account
- Wait for admin approval
- Login after approval
- View available books
- Search books by title, author, or ISBN
- Borrow books (14-day limit)
- View due dates and current fines
- Return borrowed books
- Pay fines at library counter
- Mark fines as paid after payment

### For Admins:
- View pending student registrations
- Approve or reject student accounts
- Search books by title, author, or ISBN
- Monitor overdue books and fines
- View unpaid fines
- Manage books, students, and borrow records via /admin/
- View all books and active borrows on the dashboard
- Monitor system statistics (books, students, overdue, fines)

## Fine System

- Books must be returned within 14 days
- Late return fine: ₹1 per day after the due date
- Fines are automatically calculated when books are returned
- Students can see current fines for borrowed books
- Students must pay fines at the library counter
- After payment, students can mark fines as paid in the system
- Admin can view all overdue books and unpaid fines
