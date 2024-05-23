from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .forms import RegistrationForm
from .models import Employee

def login_user(request):
    if request.method == "POST":
        employeeID = request.POST['employeeID']
        password = request.POST['password']
        user = authenticate(request, username=employeeID, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'Login.html', {})

@login_required
def home(request):
    return render(request, 'Home.html', {})

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Employee.objects.create(
                user=user,
                employeeID=form.cleaned_data['employeeID'],
                position=form.cleaned_data['position']
            )
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'Register.html', {'form': form})