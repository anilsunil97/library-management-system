"""
Fix database connection issues
Run this with: python fix_database.py
"""
import os
import sys
import shutil
from pathlib import Path

def fix_database():
    print("🔧 Fixing database issues...\n")
    
    db_file = Path('db.sqlite3')
    
    # Check if database exists
    if not db_file.exists():
        print("❌ Database file not found!")
        print("Run: python manage.py migrate")
        return
    
    print(f"✓ Database file found: {db_file}")
    print(f"  Size: {db_file.stat().st_size} bytes")
    
    # Check for lock files
    lock_files = [
        'db.sqlite3-journal',
        'db.sqlite3-wal',
        'db.sqlite3-shm'
    ]
    
    print("\n📋 Checking for lock files...")
    for lock_file in lock_files:
        if Path(lock_file).exists():
            print(f"  ⚠️  Found: {lock_file}")
            try:
                os.remove(lock_file)
                print(f"  ✓ Removed: {lock_file}")
            except Exception as e:
                print(f"  ❌ Could not remove {lock_file}: {e}")
        else:
            print(f"  ✓ No {lock_file}")
    
    # Test database connection
    print("\n🔌 Testing database connection...")
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
        django.setup()
        
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        
        # Check tables
        from django.contrib.auth.models import User
        from library.models import Student, Book
        
        print(f"\n📊 Database stats:")
        print(f"  Users: {User.objects.count()}")
        print(f"  Students: {Student.objects.count()}")
        print(f"  Books: {Book.objects.count()}")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\n💡 Solutions:")
        print("1. Stop the Django development server")
        print("2. Close any database browser tools")
        print("3. Run: python manage.py migrate")
        print("4. Restart the server")
        return
    
    print("\n✅ Database is working correctly!")
    print("\n💡 If you still get errors:")
    print("1. Stop the development server (Ctrl+C)")
    print("2. Run this script again")
    print("3. Start the server: python manage.py runserver")

if __name__ == '__main__':
    fix_database()
