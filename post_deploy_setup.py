"""
Post-deployment setup script
Run this after deploying to create initial data
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from django.contrib.auth.models import User
from library.models import Student, Book

def setup():
    print("🚀 Post-Deployment Setup")
    print("=" * 50)
    
    # Create admin user
    print("\n1. Creating admin user...")
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'is_staff': True,
            'is_superuser': True,
            'email': 'admin@library.com'
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("   ✅ Admin created: username=admin, password=admin123")
    else:
        print("   ℹ️  Admin user already exists")

    # Create sample student
    print("\n2. Creating sample student...")
    student_user, created = User.objects.get_or_create(
        username='student1',
        defaults={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@student.com'
        }
    )
    if created:
        student_user.set_password('student123')
        student_user.save()
        Student.objects.create(
            user=student_user,
            student_id='STU001',
            roll_no='ROLL001',
            phone='1234567890',
            is_approved=True
        )
        print("   ✅ Student created: username=student1, password=student123")
    else:
        print("   ℹ️  Student user already exists")

    # Create sample books
    print("\n3. Creating sample books...")
    books_data = [
        {
            'title': 'Python Programming',
            'author': 'John Smith',
            'isbn': '9781234567890',
            'quantity': 5,
            'available': 5
        },
        {
            'title': 'Django for Beginners',
            'author': 'Jane Doe',
            'isbn': '9781234567891',
            'quantity': 3,
            'available': 3
        },
        {
            'title': 'Web Development',
            'author': 'Bob Johnson',
            'isbn': '9781234567892',
            'quantity': 4,
            'available': 4
        },
        {
            'title': 'Database Design',
            'author': 'Alice Williams',
            'isbn': '9781234567893',
            'quantity': 3,
            'available': 3
        },
        {
            'title': 'Software Engineering',
            'author': 'Charlie Brown',
            'isbn': '9781234567894',
            'quantity': 2,
            'available': 2
        },
    ]

    books_created = 0
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            isbn=book_data['isbn'],
            defaults=book_data
        )
        if created:
            books_created += 1
    
    print(f"   ✅ {books_created} books created")
    print(f"   ℹ️  Total books in system: {Book.objects.count()}")

    print("\n" + "=" * 50)
    print("✅ Setup Complete!")
    print("\n📝 Login Credentials:")
    print("   Admin: admin / admin123")
    print("   Student: student1 / student123")
    print("\n🌐 Access your application and start using it!")

if __name__ == '__main__':
    try:
        setup()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure migrations are run first:")
        print("   python manage.py migrate")
