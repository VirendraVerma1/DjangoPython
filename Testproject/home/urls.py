"""Firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home"),
    path('index', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('login', views.loginUser,name="login"),
    path('logout', views.logoutUser,name="logout"),
    path('blogform', views.blogform,name="blogform"),
    path('blogtag', views.blogform,name="blogtag"),
    path('blogtagsubmit', views.blogform,name="blogtagsubmit"),
    path('blogpost/<int:idd>', views.blogpost,name="blogpost"),
    path('blogpostdelete/<int:idd>', views.blogpostdelete,name="blogpostdelete"),
    path('blogpostupdate/<int:idd>', views.blogpostupdate,name="blogpostupdate"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
