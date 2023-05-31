from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'dictionary.html', {'fname': fname})
            
        else:
            messages.error(request, "Wrong Credentials!!!")
            return redirect('index')
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username is already exist")
            return redirect('register')
            
        if User.objects.filter(email=email):
            messages.error(request, "Email is already exist")
            return redirect('register')
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters!")
            
        if pass1!=pass2:
            messages.error(request, "Password Mismatch!")
            
        if not username.isalnum():
            messages.error(request, "The username must be alpha numeric!")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email. Please confirm email in order to activate your account")
        
        return redirect('index')
    return render(request, 'register.html')

def LogOut(request):
    logout(request)
    return redirect('index')

def meaning(request):
    return render(request, 'dictionary.html')

def translate(request):
    return render(request, 'translator.html')