from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

def index(request):
    return render(request,'index.html')

def signup(request):
    if(request.method=="POST"):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        data.save()
        return redirect('login')
    return render(request,'register.html')

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

    return render(request,'login.html')

def Home(request):
    return render(request,'index.html')