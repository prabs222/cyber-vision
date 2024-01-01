from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *


# Create your views here.

def cybervision(request):
    return render(request,"cybervision.html")



def dataset(request):
    return render(request,"dataset.html")

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm_password')
        en=Word(text=uname)
        en.save()
        if password!=cpassword:
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
        return redirect('signin')

    return render(request,"signup.html")

def signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('afterlogin')
        else:
            return redirect('signin')

    return render(request,"signin.html")

# def error_404(request,exception):
#     return render(request,"404.html")

def afterlogin(request):
    us=Word.objects.last()
    return render(request,"afterlogin.html",{'us':us})
