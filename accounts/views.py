from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

#STUDENT DASHBOARD
@login_required
def Dashboard(login_required):
    return render(login_required, 'dashboard.html')

#Student Login
def Login(request):
    return render(request, 'login.html')

#Staff Portal
def Staff(request):
    return render(request, 'staff.html')

#student
def Student(request):
    return render(request, 'student.html')
