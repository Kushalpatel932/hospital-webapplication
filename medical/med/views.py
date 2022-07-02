import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from .models import appointment, doctors, feedback

# Create your views here.
def base(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    u = feedback.objects.all()
    #u-->user
    return render(request,'services.html',{'user' : u })

def doctors_view(request):
    drs=doctors.objects.all()
    print(drs)
    
    return render(request,'doctors.html',{'dr':drs})

def departments(request):
    return render(request,'departments.html')

def contact(request):
    return render(request,'contact.html')

def appointment_view(request):
    if request.POST:
        obj = appointment()
        obj.name=request.POST['name']
        obj.email=request.POST['email']
        obj.phone=request.POST['phone']
        obj.date=request.POST['date']
        obj.department=request.POST['department']
        obj.doctor=request.POST['doctor']
        obj.message=request.POST['message']
        obj.save()
        return redirect('home')    
    return render(request,'appointment.html')
