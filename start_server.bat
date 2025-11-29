@echo off
start chrome http://127.0.0.1:8000/login/
python manage.py runserver
pause
