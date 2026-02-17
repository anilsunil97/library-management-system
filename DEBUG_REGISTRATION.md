# Debug Registration 500 Error

## Quick Fix Steps

### Step 1: Activate Virtual Environment
```cmd
myenv\Scripts\activate
```

### Step 2: Run Test Script
```cmd
python test_registration.py
```

This will show you the exact error.

### Step 3: Check Migrations
```cmd
python manage.py showmigrations library
```

If any migrations are not applied (no [X]), run:
```cmd
python manage.py migrate
```

### Step 4: Enable DEBUG Mode (Temporarily)
Create a `.env` file in your project root:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
```

Then restart your server:
```cmd
python manage.py runserver
```

Now try registering again - you'll see the actual error message.

## Common Causes of 500 Error

1. **Missing Migrations**: Database tables not created
2. **Database Locked**: SQLite file locked by another process
3. **Field Validation**: Password validators rejecting the password
4. **Missing CSRF Token**: Form security issue
5. **Database Permissions**: Can't write to db.sqlite3

## What I Fixed

I updated the `register_view` function in `library/views.py` to:
- Use `.get()` instead of direct dictionary access (prevents KeyError)
- Add `.strip()` to remove whitespace
- Validate all fields are filled
- Check for duplicate email
- Add try-except block to catch and display errors
- Better error messages

## Test the Fix

1. Activate virtual environment
2. Run: `python test_registration.py`
3. If test passes, try web registration again
4. If still failing, enable DEBUG=True to see the actual error

## Manual Database Check

```cmd
python manage.py shell
```

Then in the shell:
```python
from django.contrib.auth.models import User
from library.models import Student

# Check if tables exist
print(User.objects.count())
print(Student.objects.count())

# Try creating a test user
user = User.objects.create_user('testuser', 'test@test.com', 'testpass123')
student = Student.objects.create(user=user, student_id='TEST001', roll_no='R001', phone='1234567890')
print("Success!")
```

If this works, the issue is in the view or form submission.
