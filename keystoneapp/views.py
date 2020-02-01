from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages
from django.contrib.auth.decorators import login_required





# Create your views here.

def Index(request):
    return render(request, 'index.html')

#student registrationform
def Admission(request):
    context = {
        "form":RegistrationForm
    }
    return render(request, 'admission.html', context)

#new student registration
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

#success page
def Success(request):
    messages.add_message(request, messages.SUCCESS, "You have signup sucessfully...Proceed to Login")
    return render(request, 'success.html')

def Login(request):
    return render(request, 'login.html')

#404 page not found
def Error404(request):
    return render(request, '404.html')
