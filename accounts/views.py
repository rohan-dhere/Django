from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1 == password2:
            if User.objects.filter(username=username).exists(): #checking if user is present in db
                messages.info(request,'Username Taken')
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1) #insert into table user
                user.save() 
                return redirect('/accounts/login/')
        else:
            messages.info(request,'password not same')
            return redirect('/accounts/register')
        return redirect('/')
    
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = User.objects.get(username=username) #get username from db & check with user input
        if user.check_password(password): #get password from db & check with user input
            auth.login(request, user)
            print('login success')
            return redirect('/space')
        else:
            messages.info(request,'invalid')
            print('login invalid')
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/space')   