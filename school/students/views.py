from django.shortcuts import render,redirect
from . models import *
# Create your views here.

def addstudents(request):
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        obj=studentsregister.objects.create(sname=sname,sclass=sclass,ssession=ssession)
        obj.save()
        return redirect('viewstudents')
    return render(request,'addstudents.html')

def viewstudents(request):
    obj=studentsregister.objects.filter(status=1)
    return render(request,'viewstudents.html',{'obj':obj})

def retrievestudents(request):
    details=studentsregister.objects.all()
    return render(request,'retrieve.html',{'details':details})

def editstudents(request,id):
    object=studentsregister.objects.get(id=id)
    return render(request,'editstudents.html',{'object':object})

def update(request,id):
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        studentsregister.objects.filter(id=id).update(sname=sname,sclass=sclass,ssession=ssession)
        return redirect('viewstudents')
    
def deletestudents(request,id):
    studentsregister.objects.filter(id=id).update(status=0)
    return redirect('viewstudents')