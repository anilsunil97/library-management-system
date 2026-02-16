import os
import django
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from library.models import BorrowRecord

# Update existing borrow records with due dates
records = BorrowRecord.objects.filter(due_date__isnull=True)
for record in records:
    record.due_date = record.borrow_date + timedelta(days=14)
    record.save()
    print(f'Updated: {record.student.user.username} - {record.book.title} - Due: {record.due_date}')

print(f'\n{records.count()} borrow records updated with due dates!')
