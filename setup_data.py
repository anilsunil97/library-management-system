import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from django.contrib.auth.models import User
from library.models import Student, Book

# Create admin user
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={'is_staff': True, 'is_superuser': True}
)
if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print('Admin created: username=admin, password=admin123')

# Create student user
student_user, created = User.objects.get_or_create(
    username='student1',
    defaults={'first_name': 'John', 'last_name': 'Doe'}
)
if created:
    student_user.set_password('student123')
    student_user.save()
    Student.objects.create(user=student_user, student_id='STU001', phone='1234567890')
    print('Student created: username=student1, password=student123')

# Create sample books
books_data = [
    {'title': 'Python Programming', 'author': 'John Smith', 'isbn': '9781234567890', 'quantity': 5, 'available': 5},
    {'title': 'Django for Beginners', 'author': 'Jane Doe', 'isbn': '9781234567891', 'quantity': 3, 'available': 3},
    {'title': 'Web Development', 'author': 'Bob Johnson', 'isbn': '9781234567892', 'quantity': 4, 'available': 4},
]

for book_data in books_data:
    Book.objects.get_or_create(isbn=book_data['isbn'], defaults=book_data)

print('Sample books created')
print('\nSetup complete!')
print('Run: python manage.py runserver')
print('Login as admin: admin/admin123')
print('Login as student: student1/student123')
