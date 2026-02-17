from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.db import models
from django.http import JsonResponse
from django.conf import settings
import os
from .models import Book, Student, BorrowRecord

def register_view(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username', '').strip()
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password', '')
            confirm_password = request.POST.get('confirm_password', '')
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            student_id = request.POST.get('student_id', '').strip()
            roll_no = request.POST.get('roll_no', '').strip()
            phone = request.POST.get('phone', '').strip()
            
            # Validation
            if not all([username, email, password, confirm_password, first_name, last_name, student_id, roll_no, phone]):
                messages.error(request, 'All fields are required')
                return render(request, 'register.html')
            
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register.html')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'register.html')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'register.html')
            
            if Student.objects.filter(student_id=student_id).exists():
                messages.error(request, 'Student ID already exists')
                return render(request, 'register.html')
            
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Create student profile
            Student.objects.create(
                user=user,
                student_id=student_id,
                roll_no=roll_no,
                phone=phone,
                is_approved=False
            )
            
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'register.html')
    
    return render(request, 'register.html')

def login_view(request):
    user_type = request.GET.get('type', 'student')  # Default to student
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_type = request.POST.get('login_type', 'student')
        
        user = authenticate(request, username=username, password=password)
        if user:
            # Check if login type matches user type
            if login_type == 'admin' and not user.is_staff:
                messages.error(request, 'Invalid admin credentials. Please use student login.')
                return render(request, 'login.html', {'user_type': login_type})
            
            if login_type == 'student' and user.is_staff:
                messages.error(request, 'Admin users should use admin login.')
                return render(request, 'login.html', {'user_type': login_type})
            
            if not user.is_staff:
                try:
                    student = Student.objects.get(user=user)
                    if not student.is_approved:
                        messages.error(request, 'Your account is pending admin approval')
                        return render(request, 'login.html', {'user_type': login_type})
                except Student.DoesNotExist:
                    messages.error(request, 'Student profile not found')
                    return render(request, 'login.html', {'user_type': login_type})
            
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials')
        return render(request, 'login.html', {'user_type': login_type})
    
    return render(request, 'login.html', {'user_type': user_type})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return redirect('student_dashboard')

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
        borrowed_books = BorrowRecord.objects.filter(student=student, is_returned=False)
        returned_books = BorrowRecord.objects.filter(student=student, is_returned=True, fine_paid=False, fine_amount__gt=0)
        
        # Search functionality
        search_query = request.GET.get('search', '')
        if search_query:
            available_books = Book.objects.filter(
                available__gt=0
            ).filter(
                models.Q(title__icontains=search_query) |
                models.Q(author__icontains=search_query) |
                models.Q(isbn__icontains=search_query)
            )
        else:
            available_books = Book.objects.filter(available__gt=0)
        
        return render(request, 'student_dashboard.html', {
            'borrowed_books': borrowed_books,
            'returned_books': returned_books,
            'available_books': available_books,
            'student': student,
            'search_query': search_query
        })
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found')
        return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(
            models.Q(title__icontains=search_query) |
            models.Q(author__icontains=search_query) |
            models.Q(isbn__icontains=search_query)
        )
    else:
        books = Book.objects.all()
    
    students = Student.objects.all()
    pending_students = Student.objects.filter(is_approved=False)
    borrow_records = BorrowRecord.objects.filter(is_returned=False)
    overdue_records = [record for record in borrow_records if record.days_overdue() > 0]
    unpaid_fines = BorrowRecord.objects.filter(is_returned=True, fine_paid=False, fine_amount__gt=0)
    
    return render(request, 'admin_dashboard.html', {
        'books': books,
        'students': students,
        'pending_students': pending_students,
        'borrow_records': borrow_records,
        'overdue_records': overdue_records,
        'unpaid_fines': unpaid_fines,
        'search_query': search_query
    })

@login_required
def approve_student(request, student_id):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    student = get_object_or_404(Student, id=student_id)
    student.is_approved = True
    student.save()
    messages.success(request, f'Student {student.user.username} approved successfully')
    return redirect('admin_dashboard')

@login_required
def reject_student(request, student_id):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    student = get_object_or_404(Student, id=student_id)
    student.is_approved = False
    student.save()
    messages.warning(request, f'Student {student.user.username} rejected')
    return redirect('admin_dashboard')

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    student = get_object_or_404(Student, user=request.user)
    
    if book.available > 0:
        BorrowRecord.objects.create(student=student, book=book)
        book.available -= 1
        book.save()
        messages.success(request, f'Successfully borrowed {book.title}')
    else:
        messages.error(request, 'Book not available')
    return redirect('student_dashboard')

@login_required
def return_book(request, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id)
    record.is_returned = True
    record.return_date = timezone.now()
    
    # Calculate fine
    fine = record.calculate_fine()
    record.fine_amount = fine
    record.save()
    
    # Update student's total fine
    if fine > 0:
        student = record.student
        student.total_fine += fine
        student.save()
    
    book = record.book
    book.available += 1
    book.save()
    
    if fine > 0:
        messages.warning(request, f'Book returned! Fine: ₹{fine} (Pay at library counter)')
    else:
        messages.success(request, f'Successfully returned {book.title}')
    return redirect('student_dashboard')

@login_required
def pay_fine(request, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id)
    if record.fine_amount > 0 and not record.fine_paid:
        record.fine_paid = True
        record.save()
        
        # Deduct from student's total fine
        student = record.student
        student.total_fine -= record.fine_amount
        student.save()
        
        messages.success(request, f'Fine of ₹{record.fine_amount} paid successfully!')
    return redirect('student_dashboard')


def debug_database(request):
    """Debug view to check database configuration"""
    db_config = settings.DATABASES['default']
    
    info = {
        'database_engine': db_config.get('ENGINE', 'Not set'),
        'database_name': db_config.get('NAME', 'Not set'),
        'database_host': db_config.get('HOST', 'Not set'),
        'has_database_url': 'Yes' if os.environ.get('DATABASE_URL') else 'No',
        'is_vercel': 'Yes' if os.environ.get('VERCEL') else 'No',
        'database_url_preview': os.environ.get('DATABASE_URL', 'Not set')[:50] + '...' if os.environ.get('DATABASE_URL') else 'Not set',
    }
    
    # Try to connect
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        info['connection_test'] = 'SUCCESS'
        
        # Try to query auth_user
        try:
            from django.contrib.auth.models import User
            info['user_count'] = User.objects.count()
            info['auth_user_table'] = 'EXISTS'
        except Exception as e:
            info['auth_user_table'] = f'ERROR: {str(e)}'
            info['user_count'] = 'N/A'
            
    except Exception as e:
        info['connection_test'] = f'FAILED: {str(e)}'
    
    return JsonResponse(info, json_dumps_params={'indent': 2})
