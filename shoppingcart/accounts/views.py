from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        pswd1=request.POST['password1']
        pswd2=request.POST['password2']
        if pswd1==pswd2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('accounts:register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=pswd1,email=email)
                user.save();
                print("User Created")
                return redirect('shopapp:allProductsCat')
        else:
            print("Password Not Matched")
            messages.info(request, "Password Not Matched")
            return redirect('accounts:register')
    else:
        return render(request,'registration.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("User Created")
            return redirect('shopapp:allProductsCat')
        else:
            messages.info(request, "You entered invalid details,Please try again with valid username and password")
            return redirect('accounts:login')

    else:
        return render(request,'login.html')



def checkoutLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("User Created")
            return redirect('shopapp:allProductsCat')
        else:
            messages.info(request, "You entered invalid details,Please try again with valid username and password")
            return redirect('accounts:checkoutLogin')

    else:
        return render(request,'checkout_login.html')



def logout(request):
    auth.logout(request)
    return redirect('shopapp:allProductsCat')


        