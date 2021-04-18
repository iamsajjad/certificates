
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
    sclass = request.POST.get('sclass', 'Unknow')

    m1 = request.POST.get('m1', 'Unknow')
    m2 = request.POST.get('m2', 'Unknow')
    m3 = request.POST.get('m3', 'Unknow')
    m4 = request.POST.get('m4', 'Unknow')
    m5 = request.POST.get('m5', 'Unknow')
    m6 = request.POST.get('m6', 'Unknow')
    m7 = request.POST.get('m7', 'Unknow')

    d1 = request.POST.get('d1', 'Unknow')
    d2 = request.POST.get('d2', 'Unknow')
    d3 = request.POST.get('d3', 'Unknow')
    d4 = request.POST.get('d4', 'Unknow')
    d5 = request.POST.get('d5', 'Unknow')
    d6 = request.POST.get('d6', 'Unknow')
    d7 = request.POST.get('d7', 'Unknow')

    new_student = Student.objects.create(
            name = name,
            college=college)

    new_grades = Grades.objects.create(
            sclass=sclass,
            m1=m1,
            d1=d1,
            m2=m2,
            d2=d2,
            m3=m3,
            d3=d3,
            m4=m4,
            d4=d4,
            m5=m5,
            d5=d5,
            m6=m6,
            d6=d6,
            m7=m7,
            d7=d7)
    new_student.grades.add(new_grades)
    new_grades.save()
    new_student.save()

    students = Student.objects.all()

    response = {
        'students' : students
    }

    return render(request, 'graduates/Graduates.html', response)

@login_required(login_url='/account/')
def studentProfile(request, pk):

    student = Student.objects.get(id=pk)

    response = {
        'student' : student
    }

    return render(request, 'graduates/studentProfile.html', response)
