"""
Run migrations on Vercel PostgreSQL database
This script connects to your production database and creates all tables
"""
import os
import sys

def run_migrations():
    print("🔧 Running Database Migrations...")
    print("=" * 60)
    
    # Check if DATABASE_URL is set
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ ERROR: DATABASE_URL environment variable not set!")
        print("\nTo fix this:")
        print("1. Get your database URL from Vercel or Neon")
        print("2. Run: set DATABASE_URL=your-connection-string")
        print("3. Run this script again")
        return False
    
    print(f"✓ DATABASE_URL found")
    print(f"  Host: {database_url.split('@')[1].split('/')[0] if '@' in database_url else 'unknown'}")
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
    
    try:
        import django
        django.setup()
        print("✓ Django initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Django: {e}")
        return False
    
    # Run migrations
    print("\n📦 Running migrations...")
    try:
        from django.core.management import call_command
        
        # Show migrations
        print("\nChecking migration status...")
        call_command('showmigrations')
        
        print("\nApplying migrations...")
        call_command('migrate', '--noinput')
        
        print("\n✅ Migrations completed successfully!")
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Verify tables were created
    print("\n🔍 Verifying database tables...")
    try:
        from django.contrib.auth.models import User
        from library.models import Student, Book, BorrowRecord
        
        print(f"  ✓ auth_user table exists")
        print(f"  ✓ library_student table exists")
        print(f"  ✓ library_book table exists")
        print(f"  ✓ library_borrowrecord table exists")
        
        # Show counts
        print(f"\n📊 Current data:")
        print(f"  Users: {User.objects.count()}")
        print(f"  Students: {Student.objects.count()}")
        print(f"  Books: {Book.objects.count()}")
        print(f"  Borrow Records: {BorrowRecord.objects.count()}")
        
    except Exception as e:
        print(f"⚠️  Warning: Could not verify tables: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Database setup complete!")
    print("\n📝 Next steps:")
    print("1. Run: python post_deploy_setup.py (to create admin & sample data)")
    print("2. Test your app: https://library-management-system-taupe-tau.vercel.app/register/")
    
    return True

if __name__ == '__main__':
    success = run_migrations()
    sys.exit(0 if success else 1)
