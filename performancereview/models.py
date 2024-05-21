from django.db import models
import datetime

#Categories of Products - class and then the attributes
class Category(models.Model):
	name = models.CharField(max_length=50)

	#Needs this for it to appear on the website
	def __str__(self): 
		return self.name

	#Make 'categorys' be displayed as 'categories'
	class Meta:
		verbose_name_plural ='categories'

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

#All our products
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
	#category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='uploads/product/')
	
	def __str__(self): 
		return self.name

#Customer Orders
class Order(models.Model):
	#product = models.ForeignKey(Product, on_delete=models.CASCADE)
	#customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	address = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=30, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self): 
		return self.name

#Employee
class Employee(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	employeeID = models.CharField(max_length=30, primary_key=True)
	address = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=10, blank=True)
	email = models.EmailField(max_length=100)
	position = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads/employee/', default='')
	password = models.CharField(max_length=100, blank=True, null=True)
	hireDate = models.CharField(max_length=50, blank=True, null=True)
	#gender = models.CharField(max_length=20)
	#dateOfBirth = models.CharField(max_length=50)	
	#is_ceo = models.BooleanField(default=False)
	#is_dev = models.BooleanField(default=False)
	#is_hr = models.BooleanField(default=False)
	#is_supervisor = models.BooleanField(default=False)
	#salary = models.DecimalField(default=0, decimal_places=2, max_digits=9, blank=True)

	# def __str__(self): 
	# 	return self.name

	# def __str__(self):
	# 	return f'{self.first_name} {self.last_name}'
	
	def __str__(self): 
		return self.employeeID

#Performance Review forms (include PR form attributes)
class PerformanceReview(models.Model): 
	employeeName = models.CharField(max_length=100) 
	#employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	#employeeID = models.CharField(max_length=30)
	employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
	position = models.CharField(max_length=50)
	dateOfReview = models.DateField(max_length=30)
	timeOfReview = models.TimeField(max_length=30)
	jobKnowledge = models.CharField(max_length=30)
	workQuality = models.CharField(max_length=30)
	initiative = models.CharField(max_length=30)
	communication = models.CharField(max_length=30)
	dependability = models.CharField(max_length=30)
	overallFeedback = models.TextField(max_length=2000, blank=True, null=True)
	#employeeAccept = models.BooleanField(default=False) #Might need to edit this

	def __int__(self): 
		return self.id

#Dunder Mifflin Branches
class Branch(models.Model): 
	name = models.CharField(max_length=50)
	branchID = models.CharField(max_length=30, primary_key=True)	
	employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
	branchAddress = models.CharField(max_length=100)

	def __str__(self): 
		return self.name

	class Meta:
		verbose_name_plural ='Branches'






