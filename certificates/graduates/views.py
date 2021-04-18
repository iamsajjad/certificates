
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from student.models import Student, Grades
# Create your views here.

@login_required(login_url='/account/')
def graduatesView(request):


    students = Student.objects.all()

    response = {
        'students' : students
    }

    return render(request, 'graduates/Graduates.html', response)

@login_required(login_url='/account/')
def addStudent(request):

    name = request.POST.get('name', 'Unknow')
    college = request.POST.get('college', 'Unknow')
    new_student = Student.objects.create(
            name = name,
            college=college)

    new_student.save()

    students = Student.objects.all()

    response = {
        'students' : students
    }

    return render(request, 'graduates/Graduates.html', response)
