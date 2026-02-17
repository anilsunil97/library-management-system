@echo off
echo ========================================
echo Fix Vercel Database - Run Migrations
echo ========================================
echo.
echo STEP 1: Get your DATABASE_URL
echo.
echo 1. Go to: https://vercel.com/dashboard
echo 2. Open your project
echo 3. Click Settings ^> Environment Variables
echo 4. Find DATABASE_URL
echo 5. Click the eye icon to reveal it
echo 6. Copy the ENTIRE value
echo.
echo STEP 2: Paste it below when prompted
echo.
set /p DATABASE_URL="Paste your DATABASE_URL here: "
echo.
echo ========================================
echo Running migrations...
echo ========================================
echo.

REM Activate virtual environment
call myenv\Scripts\activate.bat

REM Run migrations
python run_migrations.py

echo.
echo ========================================
echo Creating admin user and sample data...
echo ========================================
echo.

REM Run setup
python post_deploy_setup.py

echo.
echo ========================================
echo DONE! Test your app now:
echo https://library-management-system-taupe-tau.vercel.app/register/
echo ========================================
echo.
pause
