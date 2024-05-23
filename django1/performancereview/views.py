from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, PerformanceReview
#Django already has login and logout functionality
from django.contrib.auth import authenticate, login, logout
#Displays error messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.db.models import Q


from .forms import PerformanceReviewForm


def update_user(request):
	return render(request, 'update_user.html', {})

def performancereviewform(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            employeeID = form.cleaned_data['employeeID']
            employee = get_object_or_404(Employee, employeeID=employeeID)
            
            # Create a new performance review object using the cleaned data
            newPR = PerformanceReview(
                employeeName=form.cleaned_data['employeeName'],
                employeeID=employee,  # Assign the Employee instance
                position=form.cleaned_data['position'],
                dateOfReview=form.cleaned_data['dateOfReview'],
                timeOfReview=form.cleaned_data['timeOfReview'],
                jobKnowledge=form.cleaned_data['jobKnowledge'],
                workQuality=form.cleaned_data['workQuality'],
                initiative=form.cleaned_data['initiative'],
                communication=form.cleaned_data['communication'],
                dependability=form.cleaned_data['dependability'],
                overallFeedback=form.cleaned_data['overallFeedback'],
            )
            newPR.save()
            messages.success(request, "Successfully created Performance Review")
            return redirect('home')  # Replace with your success URL
        else:
            messages.error(request, "There was an error. Please try again.")
            return redirect('performancereviewform')
    else:
        form = PerformanceReviewForm()
    
    return render(request, 'performancereviewform.html', {'form': form})





def employee(request, employeeID):
    try:
        # Get the specific employee based on the provided employeeID
        employee = Employee.objects.get(employeeID=employeeID)
        
        # Get all performance reviews for the specific employee and order them by review date (most recent at top)
        performancereviews = PerformanceReview.objects.filter(employeeID=employee).order_by('-dateOfReview')

        return render(request, 'employee.html', {
            'employee': employee,
            'performancereviews': performancereviews
        })
    except Employee.DoesNotExist:
        # Handle the case where the employee does not exist
        messages.error(request, "Employee not found.")
        return redirect('home')


def performancereviewdisplay(request, id):
    performancereview = get_object_or_404(PerformanceReview, id=id)
    return render(request, 'performancereviewdisplay.html', {
        'performancereview': performancereview
    })


def home(request):
	# employees = Employee.objects.all()
	# employees = Employee.objects.all().order_by('first_name', 'last_name')
	# return render(request, 'home.html', {'employees':employees})
	return render(request, 'home.html', {})

# def employees1(request):
# 	employees = Employee.objects.all().order_by('first_name', 'last_name')
# 	return render(request, 'employees1.html', {'employees':employees})

def employees1(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).order_by('first_name', 'last_name')
    else:
        employees = Employee.objects.all().order_by('first_name', 'last_name')
    
    return render(request, 'employees1.html', {'employees': employees, 'query': query})


def about(request):
	return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        employeeID = request.POST['employeeID']
        password = request.POST['password']
        user = authenticate(request, username=employeeID, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error. Please try again."))
            return redirect('login')
    else:
        return render(request, 'Login.html', {})



def logout_user(request):
	logout(request)
	# messages.success(request, ("Successfully logged out."))
	return redirect('login')

#Commented out for testing
# def performancereviewform(request):
# 	return render(request, 'performancereviewform.html', {})

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
			#login(request, user)
			messages.success(request, ("Successfully registered account."))
			return redirect('home')
		else:
			messages.success(request, ("Oops! There was a problem registering. Please try again."))
			return redirect('register')
	else: 
		return render(request, 'register.html', {'form':form})


