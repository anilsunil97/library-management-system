from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
    path('pay-fine/<int:record_id>/', views.pay_fine, name='pay_fine'),
    path('approve-student/<int:student_id>/', views.approve_student, name='approve_student'),
    path('reject-student/<int:student_id>/', views.reject_student, name='reject_student'),
    path('debug-db/', views.debug_database, name='debug_database'),  # Debug endpoint
]
