#from django.shortcuts import render,request
#from .models import Book
# Create your views here.
# views.py

from django.shortcuts import render
from.models import Book
from.forms import BookForm,BForm


# Create your views here.
def show(request):
    return render(request,"home.html")

def register(request):
    title="Student Registeration"
    form=BookForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        clas=form.cleaned_data['s_class']
        addr=form.cleaned_data['s_address']
        school=form.cleaned_data['s_School']
        mail=form.cleaned_data['s_email']
        email=Book.objects.filter(s_email=mail)
        if len(email)>0:
            return render(request,'ack.html',{"title":"Student Already exists...Try with another email"})
        else:
            p=Book(s_name=name,s_class=clas,s_address=addr,s_School=school,s_email=mail)
            p.save()
            return render(request,'ack.html',{"title":"Registered Successfully"})
    context={
    "title":title,
    "form":form,
    } 
    return render(request,'register.html',context) 



def existing(request):
    title="All registered students"
    queryset=Book.objects.all()
    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context) 

def Search(request):
    title="Search Student"
    form=BForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=Book.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':"Student details not found..."})
        
        context={
            'title':title,
            'queryset':queryset,

        }
        return render(request,'existing.html',context) 

    context={
            'title':title,
            'form':form,
    } 
    return render(request,'Search.html',context)   


def dropout(request):
    title="Drop Out"
    form=BForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=Book.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':"student details Not found...please enter valid email"})
        else:
            queryset=Book.objects.filter(s_name=name).delete()
            return render(request,'ack.html',{'title':"Student removed from database"})
    context={
    'title':title,
    'form':form,
    } 
    return render(request,'drop.html',context)     
        











