import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from library.models import Student

# Update existing students
students = Student.objects.all()
for student in students:
    if not student.roll_no or student.roll_no == 'N/A':
        student.roll_no = f'ROLL{student.id:03d}'
    student.is_approved = True
    student.save()
    print(f'Updated: {student.user.username} - Roll No: {student.roll_no}, Approved: {student.is_approved}')

print('\nAll existing students updated and approved!')
