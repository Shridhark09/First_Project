from django.contrib import messages
from django.shortcuts import render, redirect
from ..registration.models import Student
from.models import Reports
# Create your views here.x
def reports(request):
    reports = Reports.objects.all()
    return render(request, 'dashboard.html', {"reports": reports})


def addScore(request):
    studentList = Student.objects.raw('Select * from registration_student where id not in (select student_id from performance_reports)')
    return render(request,'addScore.html',{'studentList': studentList})

def saveScore(request):
    r=Reports()
    r.tasks=request.POST.get("tasks")
    r.quizz=request.POST.get("quizz")
    r.LinkdIn=request.POST.get("LinkdIn")
    r.presentation =request.POST.get("presentation")

    sid= request.POST.get('student')
    student=Student.objects.get(id=sid)
    r.name = student.name
    r.student=student

    r.save()
    messages.success(request,"Student Score Added Successfully")
    return redirect('/reports')


def dashboard(request):
    reports=Reports.objects.all()
    return render(request,'dashboard.html',{"reports": reports})


def updateScore(request,pk):
    score=Reports.objects.get(id=pk)
    return render(request,'updateScore.html',{'score': score})

def saveUpdatedScore(request,pk):
    r= Reports.objects.get(id=pk)
    r.tasks = request.POST.get("tasks")
    r.quizz = request.POST.get("quizz")
    r.LinkdIn = request.POST.get("LinkdIn")
    r.presentation = request.POST.get("presentation")

    r.save()  #update details
    messages.success(request,f"You have updated details successfully")
    return redirect('/reports')
