from django.shortcuts import render, redirect
from .models import Employee
#Django already has login and logout functionality
from django.contrib.auth import authenticate, login, logout
#Displays error messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms




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

#We need passwords that are less than 8 characters in length RIP
def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			#log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Successfully registered account."))
			return redirect('home')
		else:
			messages.success(request, ("Oops! There was a problem registering. Please try again."))
			return redirect('register')
	else: 
		return render(request, 'register.html', {'form':form})


