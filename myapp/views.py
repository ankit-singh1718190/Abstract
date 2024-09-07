from django.shortcuts import render
from .models import Student,Teacher,Contractor
# Create your views here.
def StudemtFun(request):
    students=Student.objects.all()
    teachers = Teacher.objects.all()
    contractors = Contractor.objects.all()
    context={
        'students':students,
        'teachers': teachers,
        'contractors': contractors,
    }
    return render(request,'myapp/home.html',context)