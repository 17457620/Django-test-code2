from django.shortcuts import render, redirect
from .models import Employee
#Django already has login and logout functionality
from django.contrib.auth import authenticate, login, logout
#Displays error messages
from django.contrib import messages


def home(request):
	employees = Employee.objects.all()
	return render(request, 'home.html', {'employees':employees})

def about(request):
	return render(request, 'about.html', {})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("Successfully logged in."))
			return redirect('home')
		else: 
			messages.success(request, ("There was an error. Please try again."))
			return redirect('login')
			
	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("Successfully logged out."))
	return redirect('home')

def performancereviewform(request):
	return render(request, 'performancereviewform.html', {})




