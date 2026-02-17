"""
Comprehensive SQLite fix for Windows
Run with: python fix_sqlite_issue.py
"""
import os
import sqlite3
import sys
from pathlib import Path

def fix_sqlite():
    print("🔧 Fixing SQLite database issues...\n")
    
    db_path = Path('db.sqlite3')
    
    if not db_path.exists():
        print("❌ Database file not found!")
        print("Run: python manage.py migrate")
        return False
    
    print(f"✓ Database found: {db_path}")
    print(f"  Size: {db_path.stat().st_size} bytes")
    print(f"  Read-only: {not os.access(db_path, os.W_OK)}")
    
    # Remove lock files
    print("\n🗑️  Removing lock files...")
    lock_files = ['db.sqlite3-journal', 'db.sqlite3-wal', 'db.sqlite3-shm']
    for lock_file in lock_files:
        if Path(lock_file).exists():
            try:
                os.remove(lock_file)
                print(f"  ✓ Removed: {lock_file}")
            except Exception as e:
                print(f"  ❌ Could not remove {lock_file}: {e}")
    
    # Test direct SQLite connection
    print("\n🔌 Testing direct SQLite connection...")
    try:
        conn = sqlite3.connect(str(db_path), timeout=30)
        cursor = conn.cursor()
        
        # Check WAL mode
        cursor.execute("PRAGMA journal_mode")
        journal_mode = cursor.fetchone()[0]
        print(f"  Current journal mode: {journal_mode}")
        
        # Switch to DELETE mode (better for Windows)
        if journal_mode.upper() != 'DELETE':
            print(f"  Switching from {journal_mode} to DELETE mode...")
            cursor.execute("PRAGMA journal_mode=DELETE")
            new_mode = cursor.fetchone()[0]
            print(f"  ✓ New journal mode: {new_mode}")
        
        # Test write operation
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER)")
        cursor.execute("INSERT INTO test_table VALUES (1)")
        conn.commit()
        cursor.execute("DELETE FROM test_table")
        conn.commit()
        cursor.execute("DROP TABLE test_table")
        conn.commit()
        
        print("  ✓ Write test successful!")
        
        conn.close()
        print("✅ Direct SQLite connection works!\n")
        
    except sqlite3.OperationalError as e:
        print(f"❌ SQLite error: {e}")
        print("\n💡 The database file might be locked by another process.")
        print("   Close all programs that might be using it:")
        print("   - DB Browser for SQLite")
        print("   - Django development server")
        print("   - Any Python processes")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    # Test Django connection
    print("🐍 Testing Django connection...")
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
        import django
        django.setup()
        
        from django.db import connection
        from django.contrib.auth.models import User
        
        # Test query
        user_count = User.objects.count()
        print(f"  ✓ Django connection works!")
        print(f"  Users in database: {user_count}")
        
        # Test write
        test_user = User.objects.filter(username='__test_user__').first()
        if test_user:
            test_user.delete()
        
        test_user = User.objects.create_user(
            username='__test_user__',
            email='test@test.com',
            password='testpass123'
        )
        print(f"  ✓ Write test successful!")
        test_user.delete()
        print(f"  ✓ Delete test successful!")
        
        print("✅ Django database access works!\n")
        
    except Exception as e:
        print(f"❌ Django error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print("\n📝 Next steps:")
    print("1. Stop your development server (Ctrl+C)")
    print("2. Start it again: python manage.py runserver")
    print("3. Try registration in your browser")
    print("\nIf it still fails, the issue is with concurrent access.")
    print("Consider using PostgreSQL for production.")
    
    return True

if __name__ == '__main__':
    success = fix_sqlite()
    sys.exit(0 if success else 1)
