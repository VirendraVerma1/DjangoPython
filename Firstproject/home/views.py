from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

from home.forms import BlogFrom

# Create your views here.


def index(request):
    
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        
        contacts=Contact.objects.all()
        context={
            'contacts':contacts
        }

        return render(request,'index.html',context)
    
    # return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')

def contact(request):
    if(request.method=="POST"):
        namee=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        desc=request.POST['desc']
        contact=Contact(name=namee,phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()
        
    return render(request,'contact.html')


def loginUser(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")

        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def blogpost(request,idd):
    contact=Contact.objects.get(id=idd)
    # contact.name="Test"
    # contact.save()
    context={
            'contact':contact
        }
    return render(request,'blogpost.html',context)


def blogs(request):
    return render(request,'blogs.html')

def blog(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        form=BlogFrom()
        if(request.method == 'POST'):
            form=BlogFrom(request.POST,request.FILES)
            # print(form.fields.get('image'))
            # form.fields.get('title')
            if(form.is_valid()):
                print("validated")
                form.save()
            else:
                print(form.errors)
            return render(request, 'contact.html')
        else:
            context={
                'form':form
            }
            return render(request, 'blogform.html',context)

