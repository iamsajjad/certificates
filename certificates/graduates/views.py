
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from pyqrcode import QRCode
from student.models import Student
from author.models import UserSettings
# Create your views here.

# make QR code
def qrCodeGen(student):

    primary = student.id
    name = student.name
    date = datetime.now().year
    d1 = student.d1
    d2 = student.d2
    d3 = student.d3
    d4 = student.d4
    d5 = student.d5
    d6 = student.d6
    d7 = student.d7
    avg = student.avg


    QRdata = str("""
    Information Technology Certificate

    ID : {0}
    Student Name : {1}
    Year : {2}

    ++++++++++++++++++++

    Web Programming : {3}
    Data communiction : {4}
    Linux Operating System : {5}
    Wan Technology : {6}
    Planning For Information Network : {7}
    English : {8}
    Project : {9}

    ++++++++++++++++++++

    Average : {10}

    """.format(primary, name, date, d1, d2, d3,
               d4, d5, d6, d7, avg))

    QRobject = QRCode(QRdata, encoding='utf-8')
    QRobject.svg("static/temporary/cluster.svg", scale = 1)

@login_required(login_url='/account/')
def graduatesView(request):

    students = Student.objects.all()
    settings = UserSettings.objects.get(id=request.user.id)

    response = {
        'students' : students,
        'settings' : settings
    }

    return render(request, 'graduates/Graduates.html', response)

@login_required(login_url='/account/')
def addStudent(request):

    settings = UserSettings.objects.get(id=request.user.id)

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

    d1 = float(request.POST.get('d1', 'Unknow'))
    d2 = float(request.POST.get('d2', 'Unknow'))
    d3 = float(request.POST.get('d3', 'Unknow'))
    d4 = float(request.POST.get('d4', 'Unknow'))
    d5 = float(request.POST.get('d5', 'Unknow'))
    d6 = float(request.POST.get('d6', 'Unknow'))
    d7 = float(request.POST.get('d7', 'Unknow'))

    avg = float(sum([d1, d2, d3, d4, d5, d6, d7]) / 7)

    new_student = Student.objects.create(
        name = name,
        college=college,
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
        d7=d7,
        avg=avg)
    new_student.save()

    students = Student.objects.all()

    response = {
        'students' : students,
        'settings' : settings
    }
    return HttpResponseRedirect('/graduates/')

@login_required(login_url='/account/')
def studentProfile(request, pk):

    student = Student.objects.get(id=pk)
    settings = UserSettings.objects.get(id=request.user.id)

    response = {
        'student' : student,
        'settings' : settings
    }

    return render(request, 'graduates/studentProfile.html', response)

@login_required(login_url='/account/')
def printPage(request, pk):

    student = Student.objects.get(id=pk)
    settings = UserSettings.objects.get(id=request.user.id)
    QRcode = qrCodeGen(student)

    response = {
        'student' : student,
        'settings' : settings
    }

    return render(request, 'graduates/printPage.html', response)

@login_required(login_url='/account/')
def delete(request, pk):

    student = Student.objects.get(id=pk)
    student.delete()

    return HttpResponseRedirect('/graduates/')

