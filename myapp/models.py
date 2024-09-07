from django.db import models

# Student Model
#abstract
class CommanInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        abstract=True

class Student(CommanInfo):
    roll = models.IntegerField(unique=True)  # Assuming roll numbers are unique
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()

# Teacher Model
class Teacher(CommanInfo):
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Assuming email is unique for each teacher
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    hire_date = models.DateField()

# Contractor Model (with payment details)
class Contractor(CommanInfo):
    company_name = models.CharField(max_length=150)  # Contractor's company
    contact_email = models.EmailField(unique=True)  # Unique email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    address = models.TextField(blank=True, null=True)  # Optional address