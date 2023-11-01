from django.shortcuts import render,redirect
from .models import datas

# Create your views here.
def home(request):
    mydata=datas.objects.all()
    if (mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,"home.html")

def adddata(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']

        obj=datas()
        obj.name=name
        obj.age=age
        obj.address=address
        obj.contact=contact
        obj.email=email
        obj.save()
        return redirect("home")
        return render(request,"home.html")
    
def updatedata(request,id):
    mydata=datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        
        mydata.name=name
        mydata.age=age
        mydata.address=address
        mydata.contact=contact
        mydata.email=email
        mydata.save()
        return redirect("home")
    return render(request,"update.html",{'data':mydata})

def deletedata(request,id):
    mydata=datas.objects.get(id=id)
    mydata.delete()
    return redirect("home")