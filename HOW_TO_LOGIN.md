# 📖 How to Login - User Guide

## 🎯 Quick Start

### For Students

1. **Go to Login Page**
   - Visit: `http://127.0.0.1:8000/login/`
   - Student tab is selected by default (purple theme)

2. **Enter Your Credentials**
   - Username: Your student username
   - Password: Your password

3. **Click Login**
   - Button says "🔐 Login as Student"

4. **Access Dashboard**
   - You'll be redirected to your student dashboard
   - Browse books, borrow, return, and manage fines

### For Admins

1. **Go to Login Page**
   - Visit: `http://127.0.0.1:8000/login/`

2. **Switch to Admin Tab**
   - Click on "👨‍💼 Admin Login" tab
   - Theme changes to red

3. **Enter Admin Credentials**
   - Username: Your admin username
   - Password: Your admin password

4. **Click Login**
   - Button says "🔐 Login as Admin"

5. **Access Dashboard**
   - You'll be redirected to admin dashboard
   - Manage students, books, and view statistics

---

## 🆕 New Students

### Registration Process

1. **Go to Login Page**
   - Student tab is default

2. **Click "Register here"**
   - Link below the login form

3. **Fill Registration Form**
   - Personal details (name, email)
   - Student ID and Roll Number
   - Phone number
   - Create password

4. **Submit Registration**
   - You'll see success message
   - Account pending admin approval

5. **Wait for Approval**
   - Admin will review your registration
   - You'll be notified when approved

6. **Login After Approval**
   - Return to student login tab
   - Use your credentials
   - Access your dashboard

---

## 🔑 Demo Accounts

### Test Student Account
```
Tab: Student Login (purple)
Username: student1
Password: student123
```

### Test Admin Account
```
Tab: Admin Login (red)
Username: admin
Password: admin123
```

---

## ⚠️ Common Issues & Solutions

### Issue: "Invalid admin credentials"
**Problem:** Trying to use student credentials in admin login

**Solution:** 
- Switch to "Student Login" tab
- Use student credentials there

### Issue: "Admin users should use admin login"
**Problem:** Trying to use admin credentials in student login

**Solution:**
- Switch to "Admin Login" tab
- Use admin credentials there

### Issue: "Your account is pending admin approval"
**Problem:** Student account not yet approved

**Solution:**
- Wait for admin to approve your account
- Contact library admin if waiting too long
- Check your registration details

### Issue: "Student profile not found"
**Problem:** User account exists but no student profile

**Solution:**
- Contact system administrator
- May need to complete registration

### Issue: "Invalid credentials"
**Problem:** Wrong username or password

**Solution:**
- Check username spelling
- Check password (case-sensitive)
- Use correct login tab
- Try demo accounts to test

---

## 🎨 Visual Guide

### Student Login Tab (Purple Theme)
```
┌─────────────────────────────────────┐
│  [👨‍🎓 Student Login] [Admin Login]  │
├─────────────────────────────────────┤
│                                     │
│  👤 Student Username                │
│  [________________]                 │
│                                     │
│  🔒 Password                        │
│  [________________]                 │
│                                     │
│  [🔐 Login as Student]              │
│                                     │
│  New student? Register here         │
│                                     │
│  Demo: student1 / student123        │
└─────────────────────────────────────┘
```

### Admin Login Tab (Red Theme)
```
┌─────────────────────────────────────┐
│  [Student Login] [👨‍💼 Admin Login]  │
├─────────────────────────────────────┤
│                                     │
│  👨‍💼 Admin Username                 │
│  [________________]                 │
│                                     │
│  🔒 Password                        │
│  [________________]                 │
│                                     │
│  [🔐 Login as Admin]                │
│                                     │
│  Demo: admin / admin123             │
└─────────────────────────────────────┘
```

---

## 🔄 Switching Between Login Types

### Method 1: Click Tabs
- Click "Student Login" tab for student access
- Click "Admin Login" tab for admin access

### Method 2: URL Parameters
- Student: `/login/?type=student`
- Admin: `/login/?type=admin`

---

## 📱 Mobile Users

1. **Tabs are touch-friendly**
   - Tap to switch between student/admin

2. **Form is responsive**
   - Works on all screen sizes

3. **Same functionality**
   - All features available on mobile

---

## 🎯 Login Flow Diagram

### Student Flow
```
Visit Login Page
    ↓
Student Tab (default)
    ↓
Enter Credentials
    ↓
Click "Login as Student"
    ↓
System Checks:
- Valid credentials?
- Student profile exists?
- Account approved?
    ↓
✅ Success → Student Dashboard
❌ Error → Show message
```

### Admin Flow
```
Visit Login Page
    ↓
Click "Admin Login" Tab
    ↓
Enter Admin Credentials
    ↓
Click "Login as Admin"
    ↓
System Checks:
- Valid credentials?
- User is admin?
    ↓
✅ Success → Admin Dashboard
❌ Error → Show message
```

---

## 💡 Tips

1. **Remember Your User Type**
   - Students use student tab
   - Admins use admin tab

2. **Check Tab Color**
   - Purple = Student
   - Red = Admin

3. **Read Error Messages**
   - They tell you what went wrong
   - Follow the suggestions

4. **Use Demo Accounts**
   - Test the system
   - Learn the interface

5. **Bookmark Direct Links**
   - Student: `/login/?type=student`
   - Admin: `/login/?type=admin`

---

## 🆘 Need Help?

### For Students:
- Contact library admin
- Check registration status
- Verify credentials

### For Admins:
- Check system logs
- Verify admin privileges
- Contact system administrator

---

## ✅ Quick Checklist

Before logging in:
- [ ] Know your user type (student/admin)
- [ ] Have correct credentials
- [ ] Selected correct tab
- [ ] Account is approved (students only)

After logging in:
- [ ] Redirected to correct dashboard
- [ ] Can see your information
- [ ] All features accessible

---

**Happy Learning! 📚**
