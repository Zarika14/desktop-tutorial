from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Product, ProductCategory

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

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
        # print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
        
    return render(request,'login.html')

@login_required(login_url='login')
def LogOutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Change_Password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'Change_Password.html', {'form': form})