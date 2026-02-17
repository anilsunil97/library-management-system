# Fix "Unable to Open Database File" Error

## Quick Fix (Try These in Order)

### Solution 1: Stop All Python Processes
1. Close your development server (Ctrl+C in terminal)
2. Close any database browser tools (DB Browser for SQLite, etc.)
3. Wait 5 seconds
4. Start server again: `python manage.py runserver`

### Solution 2: Run the Fix Script
```cmd
myenv\Scripts\activate
python fix_database.py
```

### Solution 3: Check File Permissions
Make sure the database file and directory are writable:
```cmd
icacls db.sqlite3
```

### Solution 4: Recreate Database (Last Resort)
⚠️ This will delete all data!

```cmd
# Backup current database
copy db.sqlite3 db.sqlite3.backup

# Delete database
del db.sqlite3

# Recreate database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Add sample data
python setup_data.py
```

## What I Fixed

Updated `library_system/settings.py` to:
- Use absolute path for database
- Disable connection pooling (conn_max_age=0)
- Increase SQLite timeout to 20 seconds
- Add SQLite-specific options to prevent locking

## Common Causes

1. **Development server still running** - Stop it with Ctrl+C
2. **Database browser open** - Close DB Browser for SQLite or similar tools
3. **Multiple Python processes** - Check Task Manager
4. **Antivirus locking file** - Add exception for project folder
5. **File permissions** - Run as administrator if needed

## Test the Fix

1. Stop the server completely
2. Activate virtual environment: `myenv\Scripts\activate`
3. Run: `python fix_database.py`
4. Start server: `python manage.py runserver`
5. Try registration again

## Still Not Working?

Run in administrator mode:
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Navigate to project: `cd C:\Users\Petpooja-1371\Desktop\LMS`
4. Activate environment: `myenv\Scripts\activate`
5. Start server: `python manage.py runserver`
