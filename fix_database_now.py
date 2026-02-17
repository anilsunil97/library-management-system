"""
Quick fix for Vercel database - Run this to create all tables
"""
import os
import sys

def main():
    print("=" * 70)
    print("FIX VERCEL DATABASE - CREATE TABLES")
    print("=" * 70)
    print()
    
    # Check if DATABASE_URL is already set
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        print("📋 STEP 1: Get your DATABASE_URL from Vercel")
        print()
        print("1. Go to: https://vercel.com/dashboard")
        print("2. Open your project: library-management-system")
        print("3. Click: Settings > Environment Variables")
        print("4. Find: DATABASE_URL")
        print("5. Click the eye icon to reveal the value")
        print("6. Copy the ENTIRE connection string")
        print()
        print("It should look like:")
        print("postgresql://user:pass@host.region.provider.com/db?sslmode=require")
        print()
        
        database_url = input("Paste your DATABASE_URL here: ").strip()
        
        if not database_url:
            print("\n❌ No DATABASE_URL provided. Exiting.")
            return False
        
        if not database_url.startswith('postgresql://'):
            print("\n❌ Invalid DATABASE_URL. It should start with 'postgresql://'")
            return False
        
        # Set it for this session
        os.environ['DATABASE_URL'] = database_url
        print("\n✓ DATABASE_URL set!")
    else:
        print("✓ DATABASE_URL already set in environment")
    
    print()
    print("=" * 70)
    print("RUNNING MIGRATIONS...")
    print("=" * 70)
    print()
    
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
    try:
        from django.core.management import call_command
        
        print("\n📦 Creating database tables...")
        call_command('migrate', '--noinput', verbosity=2)
        
        print("\n✅ All tables created successfully!")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Verify
    print()
    print("=" * 70)
    print("VERIFYING TABLES...")
    print("=" * 70)
    
    try:
        from django.contrib.auth.models import User
        from library.models import Student, Book, BorrowRecord
        
        print(f"✓ auth_user table: {User.objects.count()} users")
        print(f"✓ library_student table: {Student.objects.count()} students")
        print(f"✓ library_book table: {Book.objects.count()} books")
        print(f"✓ library_borrowrecord table: {BorrowRecord.objects.count()} records")
        
    except Exception as e:
        print(f"⚠️  Could not verify: {e}")
    
    # Ask about sample data
    print()
    print("=" * 70)
    print("CREATE SAMPLE DATA?")
    print("=" * 70)
    print()
    print("Do you want to create:")
    print("- Admin user (username: admin, password: admin123)")
    print("- Sample student (username: student1, password: student123)")
    print("- Sample books")
    print()
    
    create_data = input("Create sample data? (y/n): ").strip().lower()
    
    if create_data == 'y':
        print("\n📝 Creating sample data...")
        try:
            from django.contrib.auth.models import User
            from library.models import Student, Book
            
            # Create admin
            if not User.objects.filter(username='admin').exists():
                admin = User.objects.create_superuser(
                    username='admin',
                    email='admin@library.com',
                    password='admin123'
                )
                print("✓ Admin user created: admin / admin123")
            else:
                print("ℹ️  Admin user already exists")
            
            # Create sample student
            if not User.objects.filter(username='student1').exists():
                student_user = User.objects.create_user(
                    username='student1',
                    email='student@example.com',
                    password='student123',
                    first_name='John',
                    last_name='Doe'
                )
                Student.objects.create(
                    user=student_user,
                    student_id='STU001',
                    roll_no='ROLL001',
                    phone='1234567890',
                    is_approved=True
                )
                print("✓ Sample student created: student1 / student123")
            else:
                print("ℹ️  Sample student already exists")
            
            # Create sample books
            books_created = 0
            sample_books = [
                {'title': 'Python Programming', 'author': 'John Smith', 'isbn': '9781234567890', 'quantity': 5, 'available': 5},
                {'title': 'Django for Beginners', 'author': 'Jane Doe', 'isbn': '9781234567891', 'quantity': 3, 'available': 3},
                {'title': 'Web Development', 'author': 'Bob Johnson', 'isbn': '9781234567892', 'quantity': 4, 'available': 4},
            ]
            
            for book_data in sample_books:
                if not Book.objects.filter(isbn=book_data['isbn']).exists():
                    Book.objects.create(**book_data)
                    books_created += 1
            
            print(f"✓ Created {books_created} sample books")
            
        except Exception as e:
            print(f"⚠️  Error creating sample data: {e}")
    
    print()
    print("=" * 70)
    print("✅ DATABASE SETUP COMPLETE!")
    print("=" * 70)
    print()
    print("🌐 Test your app now:")
    print("   https://library-management-system-taupe-tau.vercel.app/register/")
    print()
    print("📝 Login credentials:")
    print("   Admin: admin / admin123")
    print("   Student: student1 / student123")
    print()
    
    return True

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
