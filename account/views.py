from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def SignUpPage(request):
    if request.method =='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        # print(uname,email,pass1,pass2)
        if pass1 != pass2:
            return HttpResponse("Your password does not match.")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html' )

def LoginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request,'login.html')

def HomePage(request):
    return render(request,'home.html')

