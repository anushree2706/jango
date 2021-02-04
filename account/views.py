from django.shortcuts import render
from .models import Student 

# Create your views here.
def index(request):
	if request.method == "POST":
		first_name = request.POST["fname"]
		last_name = request.POST["lname"]
		print(first_name,last_name)
		obj = Student.objects.create(first_name=first_name, last_name=last_name)
	return render(request, 'index.html')