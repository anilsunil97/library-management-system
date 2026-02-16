@echo off
echo 🚀 Library Management System - Deployment Script
echo ================================================
echo.

REM Check if vercel is installed
where vercel >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Vercel CLI is not installed.
    echo 📦 Install it with: npm install -g vercel
    exit /b 1
)

echo ✅ Vercel CLI found
echo.

REM Collect static files
echo 📦 Collecting static files...
python manage.py collectstatic --noinput --clear

echo.
echo 🚀 Deploying to Vercel...
echo.

REM Deploy
vercel --prod

echo.
echo ✅ Deployment complete!
echo.
echo ⚠️  Important Post-Deployment Steps:
echo 1. Run migrations on Vercel
echo 2. Create superuser account
echo 3. Add sample data if needed
echo.
echo 📚 See DEPLOYMENT.md for detailed instructions
pause
