from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from home.models import Contact
from home.models import Blog,Tag
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from home.forms import BlogFrom,TagForm,CreateUserForm
import json

# Create your views here.
def index(request):
    
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        if(request.GET.get('tag')!=None):
            tag=request.GET.get('tag', 1)
            blogs=Blog.objects.filter(tags_in=[tag])
        else:
            blogs=Blog.objects.all()

        contacts=Contact.objects.all()

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
                messages.add_message(request, messages.INFO, 'success')
            else:
                
                errors=form.errors.as_json()
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
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
    print(blog.tags.all())
    context={
            'blog':blog
        }
    return render(request,'blogpost.html',context)

def blogpostdelete(request,idd):
    blog=Blog.objects.get(id=idd)
    blog.delete()
    return redirect("home")

def blogpostupdate(request,idd):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        blog=Blog.objects.get(id=idd)
        form=BlogFrom(initial={'user_id':request.user.id,'username':request.user.username,'title':blog.title,'desc':blog.desc,'image':blog.image,'date':blog.date,'tags':blog.tags.all})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES,instance=blog)
            # form.data['user_id']=request.user.id
            print("filed form",form['user_id'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'success')
            else:
                print("error")
                errors=form.errors.as_json()
                errors = json.loads(errors)
                message=errors["user_id"]
                # message = json.loads(message)
                print(message)
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
        context={
                'form':form,
                'id':idd
            }
        return render(request, 'blogformedit.html',context)

#region blog tags

def blogtags(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        
        tags=Tag.objects.all()
        
        page = request.GET.get('page', 1)
        paginator = Paginator(tags, 2)

        try:
            tags = paginator.page(page)
        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)

        context={
            'tags':tags,
        }

        return render(request,'blogtagslist.html',context)

def submittag(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        form=TagForm()
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=TagForm(request.POST)
            # form.data['user_id']=request.user.id
            # print("filed form",form['user_id'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
            else:
                print(form.errors)
        
        
        context={
                'form':form
            }
        return render(request, 'blogtagslist.html',context)

#endregion
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ajaxTest(request):
    if is_ajax(request=request):
        test=request.GET.get('text')
        print(test)
        return JsonResponse({"key":"Hello world","you":"world"},status=200)
    
    else:
        return redirect("home")



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)