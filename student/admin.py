#from django.contrib import admin


#from .models import  Student

"""
class  StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
	list_filter = ('sex', 'status', 'created_time')
	search_fields =('name', 'profession')
	fieldsets =(
		(None,{
			'fields': (
				'name',
				('sex','profession'),
				('email', 'qq', 'phone'),
				'status',
			)
		}),
	)
	
admin.site.register(Student, StudentAdmin)
"""
from django.shortcuts import render

from .models import Student

def index(resquest):
	students = Student.objects.all()
	return render(resquest , 'index.html', context={'student': students})
	

# Register your models here.
