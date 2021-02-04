from django.contrib import admin

# Register your models here.
from .models import Student
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name']