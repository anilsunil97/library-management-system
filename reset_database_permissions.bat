@echo off
echo Fixing database permissions...
echo.

REM Give full control to current user
icacls db.sqlite3 /grant %USERNAME%:F

echo.
echo Database permissions updated!
echo.
echo Now try:
echo 1. Stop the server (Ctrl+C)
echo 2. Run: python manage.py runserver
echo 3. Try registration again
echo.
pause
