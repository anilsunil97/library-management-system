"""
Test script to debug registration issues
Run this with: python test_registration.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from django.contrib.auth.models import User
from library.models import Student

def test_registration():
    print("Testing registration process...")
    
    # Test data
    test_data = {
        'username': 'testuser123',
        'email': 'test@example.com',
        'password': 'testpass123',
        'first_name': 'Test',
        'last_name': 'User',
        'student_id': 'STU123',
        'roll_no': 'ROLL123',
        'phone': '1234567890'
    }
    
    try:
        # Check if user already exists
        if User.objects.filter(username=test_data['username']).exists():
            print(f"✓ User {test_data['username']} already exists, deleting...")
            User.objects.filter(username=test_data['username']).delete()
        
        if Student.objects.filter(student_id=test_data['student_id']).exists():
            print(f"✓ Student ID {test_data['student_id']} already exists, deleting...")
            Student.objects.filter(student_id=test_data['student_id']).delete()
        
        # Create user
        print("\nCreating user...")
        user = User.objects.create_user(
            username=test_data['username'],
            email=test_data['email'],
            password=test_data['password'],
            first_name=test_data['first_name'],
            last_name=test_data['last_name']
        )
        print(f"✓ User created: {user.username}")
        
        # Create student
        print("\nCreating student profile...")
        student = Student.objects.create(
            user=user,
            student_id=test_data['student_id'],
            roll_no=test_data['roll_no'],
            phone=test_data['phone'],
            is_approved=False
        )
        print(f"✓ Student created: {student.student_id}")
        print(f"  - Roll No: {student.roll_no}")
        print(f"  - Phone: {student.phone}")
        print(f"  - Approved: {student.is_approved}")
        
        print("\n✅ Registration test PASSED!")
        print("\nIf this works, the issue might be:")
        print("1. CSRF token missing in form")
        print("2. Database permissions")
        print("3. Missing migrations")
        
        # Clean up
        print("\nCleaning up test data...")
        user.delete()
        print("✓ Test data removed")
        
    except Exception as e:
        print(f"\n❌ Registration test FAILED!")
        print(f"Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_registration()
