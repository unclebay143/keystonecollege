from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages
from django.contrib.auth.decorators import login_required





#  Create your views here.

def Index(request):
    context = {
    "newslink":["American Visit to KeyStone","New Buildings to KeyStone",
                "How to become a partner","KeyStone international recognition",
                "Visit to KeyStone",]
    }
    return render(request, 'index.html',context)

# student registrationform
def Admission(request):
    context = {
        "form":RegistrationForm
    }
    return render(request, 'admission.html', context)

# new student registration
def AddStudent(request):
    
    form = RegistrationForm(request.POST)

    if form.is_valid():
        studentregister = RegistrationData(
                                           username = form.cleaned_data['username'],
                                           password = form.cleaned_data['password'],
                                           email = form.cleaned_data['email'],
                                           phone = form.cleaned_data['phone'],

        )


        studentregister.save()


    return redirect('success')

# success page


def Success(request):
    messages.add_message(request, messages.SUCCESS, "You have signup sucessfully...Proceed to ")
    return render(request, 'success.html')

def Login(request):
    return render(request, 'login.html')

# 404 page not found
def Error404(request):
    return render(request, '404.html')

def Dashboard(request):
    return render(request, 'dashboard.html')
