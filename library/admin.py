from django.contrib import admin
from .models import Student, Book, BorrowRecord

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id', 'roll_no', 'phone', 'is_approved', 'total_fine', 'registration_date']
    search_fields = ['user__username', 'student_id', 'roll_no']
    list_filter = ['is_approved', 'registration_date']
    actions = ['approve_students', 'reject_students']
    
    def approve_students(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f'{queryset.count()} students approved successfully.')
    approve_students.short_description = 'Approve selected students'
    
    def reject_students(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f'{queryset.count()} students rejected.')
    reject_students.short_description = 'Reject selected students'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'quantity', 'available']
    search_fields = ['title', 'author', 'isbn']

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'book', 'borrow_date', 'due_date', 'return_date', 'is_returned', 'fine_amount', 'fine_paid']
    list_filter = ['is_returned', 'fine_paid', 'borrow_date']
    actions = ['mark_fine_paid']
    
    def mark_fine_paid(self, request, queryset):
        queryset.update(fine_paid=True)
        self.message_user(request, f'{queryset.count()} fines marked as paid.')
    mark_fine_paid.short_description = 'Mark fine as paid'
