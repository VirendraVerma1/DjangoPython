from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.forms import BlogFrom

# Create your views here.

def index(request):
    
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        
        contacts=Contact.objects.all()
        blogs=Blog.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(blogs, 2)

        try:
            blog = paginator.page(page)
        except PageNotAnInteger:
            blog = paginator.page(1)
        except EmptyPage:
            blog = paginator.page(paginator.num_pages)

        context={
            'contacts':contacts,
            'blogs':blog,
        }

        return render(request,'index.html',context)
    
    # return render(request,'index.html',context)
    # return HttpResponse("this is homepage")


def blogform(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        form=BlogFrom(initial={'user_id':request.user.id,'username':request.user.username})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES)
            # form.data['user_id']=request.user.id
            print("filed form",form['user_id'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
            else:
                print(form.errors)
        
        
        context={
                'form':form
            }
        return render(request, 'blogform.html',context)


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
    blog=Blog.objects.get(id=idd)
    # contact.name="Test"
    # contact.save()
    print(blog.tags)
    context={
            'blog':blog
        }
    return render(request,'blogpost.html',context)





