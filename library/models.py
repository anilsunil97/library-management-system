from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    roll_no = models.CharField(max_length=20, default='N/A')
    phone = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    total_fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.username} - {self.student_id}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fine_paid = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.due_date and not self.pk:
            self.due_date = timezone.now() + timedelta(days=14)
        super().save(*args, **kwargs)
    
    def calculate_fine(self):
        if not self.due_date:
            return 0
        if self.is_returned and self.return_date:
            days_late = (self.return_date - self.due_date).days
            if days_late > 0:
                return days_late * 1  # 1 Rs per day
        else:
            # Calculate current fine if not returned
            days_late = (timezone.now() - self.due_date).days
            if days_late > 0:
                return days_late * 1
        return 0
    
    def days_overdue(self):
        if self.is_returned or not self.due_date:
            return 0
        days = (timezone.now() - self.due_date).days
        return max(0, days)
    
    def __str__(self):
        return f"{self.student.user.username} - {self.book.title}"
