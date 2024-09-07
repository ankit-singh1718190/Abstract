from django.contrib import admin
from .models import Student,Teacher,Contractor

# Register your models here.
@admin.register(Student)
class StudentAdmint(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city', 'marks', 'pass_date')  # Columns to display in admin
    search_fields = ('name', 'roll')  # Enable search by name and roll number
    list_filter = ('city', 'pass_date')  # Enable filter by city and pass date
    ordering = ('-pass_date',)  # Order by pass date, newest first
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'phone_number', 'hire_date')  # Columns to display in admin
    search_fields = ('name', 'subject')  # Enable search by name and subject
    list_filter = ('hire_date', 'subject')  # Enable filter by hire date and subject
    ordering = ('-hire_date',)  # Order by hire date, newes    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name', 'phone_number','address')  # Columns to display in admin
     # Order by due date, newest first    