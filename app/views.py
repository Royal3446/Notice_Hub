from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        get_username = request.POST.get('fname')
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        get_confirm_password = request.POST.get('confirmpassword')
        if get_password != get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/signup/')
        
        try:
            if User.objects.get(email=get_email):
                messages.warning(request,'Email is taken')
                return redirect('/signup/')
        except Exception as identifier:
            pass
        user=User.objects.create_user(username=get_username, email=get_email,password=get_password)
        print(user)
        user.save()
        messages.success(request,'User is created Please login')
        return redirect('/Login/')
    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        print(user)
        if user.exists():
            if user.first().check_password(password):                   
                login(request, user.first())
                messages.success(request, "Login success")
                return redirect('/notice/')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

def admin(request):
    return render(request,'admin_dashboard.html')

def u_profile(request):
    return render(request,'user_profile.html')

def all_notices(request):
	allnotices = Notice.objects.all()
	context = {'result':allnotices}
	return render(request,'notice.html',context)