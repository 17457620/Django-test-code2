from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class RegistrationForm(UserCreationForm):
    employeeID = forms.CharField(label="Employees ID", max_length=25)
    first_name = forms.CharField(label="Employees First Name", max_length=50)
    last_name = forms.CharField(label="Employees Last Name", max_length=50)
    email = forms.EmailField(label="Employees Work Email", max_length=100)
    position_choices = [
        ('Sales', 'Sales'),
        ('Foreman', 'Foreman'),
        ('Accounting', 'Accounting'),
        ('Warehouse', 'Warehouse'),
        ('Reception', 'Reception'),
        ('BranchManager', 'BranchManager'),
        ('HR', 'HR'),
        ('CEO', 'CEO'),
    ]
    position = forms.ChoiceField(choices=position_choices)

    class Meta:
        model = User
        fields = ('employeeID', 'first_name', 'last_name', 'email', 'position', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['employeeID']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        position = self.cleaned_data['position']
        if position in ['BranchManager', 'HR', 'CEO']:
            user.is_staff = True
            user.is_superuser = True

        if commit:
            user.save()
        return user