from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from.models import Student
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.




def login(request):
    return HttpResponseRedirect("/accounts/login")

def addStudent(request):
    return render(request,'addStudent.html')

class Register(CreateView) :
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="register.html"

def store(request):
    s=Student()
    s.name = request.POST.get('name')
    s.email= request.POST.get('email')
    s.mobile= request.POST.get('mobile')
    s.collage_name = request.POST.get('collage_name')
    s.graduate_year= request.POST.get('graduate_year')

    s.save()
    messages.success(request,"Student Added Successfully")
    return redirect('/home')

def home(request):
    studentList=Student.objects.all()
    return render(request,"home.html",{'studentList':studentList})

def deleteStudent(request,pk):
    s=Student.objects.get(id=pk)
    name=s.name
    s.delete()
    messages.success(request,f"Student '{name}'deleted successfully")
    return redirect('/home')

def updateView(request,pk):
    student=Student.objects.get(id=pk)
    return render(request,'update.html',{'s':student})

def update(request, pk):
    s=Student.objects.get(id=pk)
    s.name=request.POST.get('name')
    s.email=request.POST.get('email')
    s.mobile=request.POST.get('mobile')
    s.collage_name=request.POST.get('collage_name')
    s.graduate_year=request.POST.get('graduate_year')

    print(s.collage_name)
    print(s.name)


    s.save()
    messages.success(request,"student update successfully")
    return redirect('/home')







#
# def checkCredentials(username, password ):
#     if (username=="shridhar"and password=="admin"):
#         print("Login Sucess")



