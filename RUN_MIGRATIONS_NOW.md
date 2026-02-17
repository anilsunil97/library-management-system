# Fix "relation auth_user does not exist" Error

## What This Error Means

✅ **Good news**: Your PostgreSQL database is connected!
❌ **Problem**: The database tables haven't been created yet

You need to run Django migrations to create all the tables.

## Solution: Run Migrations

### Method 1: Using Local Script (Easiest)

1. **Get your database connection string**
   - Go to Vercel Dashboard > Your Project
   - Settings > Environment Variables
   - Find `DATABASE_URL` and click the eye icon to reveal it
   - Copy the entire value (starts with `postgresql://`)

2. **Open terminal in your project folder**
   ```cmd
   cd C:\Users\Petpooja-1371\Desktop\LMS
   ```

3. **Activate virtual environment**
   ```cmd
   myenv\Scripts\activate
   ```

4. **Set DATABASE_URL temporarily**
   ```cmd
   set DATABASE_URL=postgresql://your-connection-string-here
   ```
   (Replace with your actual connection string from step 1)

5. **Run migrations**
   ```cmd
   python run_migrations.py
   ```

6. **Create admin user and sample data**
   ```cmd
   python post_deploy_setup.py
   ```

7. **Test your app**
   Go to: https://library-management-system-taupe-tau.vercel.app/register/

### Method 2: Using Django Management Commands

If the script doesn't work, use Django directly:

```cmd
# Activate environment
myenv\Scripts\activate

# Set database URL
set DATABASE_URL=postgresql://your-connection-string-here

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Add sample data
python setup_data.py
```

### Method 3: Using Vercel CLI (Advanced)

If you have Node.js installed:

```cmd
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Link project
vercel link

# Pull environment variables
vercel env pull .env.production

# Load the environment
# On Windows CMD:
for /f "tokens=*" %i in (.env.production) do set %i

# Run migrations
python manage.py migrate

# Setup data
python post_deploy_setup.py
```

### Method 4: Direct SQL (If Nothing Else Works)

1. **Get database credentials from Vercel**
   - Settings > Environment Variables
   - Note down: host, database name, user, password

2. **Install PostgreSQL client** (if not installed)
   - Download from: https://www.postgresql.org/download/windows/

3. **Connect using psql**
   ```cmd
   psql "postgresql://user:password@host/database?sslmode=require"
   ```

4. **Run migrations manually** (not recommended, but works)
   - This is complex, use Method 1 instead

## Troubleshooting

### "DATABASE_URL not set" error

Make sure you copied the FULL connection string including:
- `postgresql://` at the start
- Username and password
- Host and port
- Database name
- `?sslmode=require` at the end

Example format:
```
postgresql://username:password@host.region.provider.com:5432/database?sslmode=require
```

### "password authentication failed"

Your connection string might have the wrong password. Get it again from:
- **Neon**: Dashboard > Connection Details
- **Vercel Postgres**: Settings > Environment Variables > POSTGRES_URL

### "could not connect to server"

- Check your internet connection
- Verify the connection string is correct
- Make sure there are no extra spaces

### "permission denied"

Make sure you're using the connection string with write permissions (not read-only).

## After Migrations Complete

Your database will have these tables:
- `auth_user` - Django users
- `auth_group` - User groups
- `auth_permission` - Permissions
- `library_student` - Student profiles
- `library_book` - Books
- `library_borrowrecord` - Borrow records
- And more Django system tables

## Verify It Worked

After running migrations, test:

1. **Go to registration page**
   https://library-management-system-taupe-tau.vercel.app/register/

2. **Fill in the form and submit**

3. **Should work now!** ✅

If you still get errors, check the Vercel deployment logs:
- Vercel Dashboard > Deployments
- Click latest deployment
- View Function Logs

## Quick Command Summary

```cmd
# Windows CMD
cd C:\Users\Petpooja-1371\Desktop\LMS
myenv\Scripts\activate
set DATABASE_URL=postgresql://your-connection-string
python run_migrations.py
python post_deploy_setup.py
```

That's it! Your database will be ready to use.
