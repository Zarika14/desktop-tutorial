from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Product, ProductCategory,Cart, CartItem
from .forms import *

# Create your views here.
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            if Product.objects.filter(
                name=product.name,
                category=product.category,
                description=product.description,
                price=product.price
            ).exists():
                messages.error(request, 'Product already exists.')
            else:
                product.save()
                product.users.add(request.user)
                return redirect('user_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


@login_required
def HomePage(request):
    products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)

    if filter_form.is_valid():
        name = filter_form.cleaned_data.get('name')
        category = filter_form.cleaned_data.get('category')

        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category=category)

    cart, created = Cart.objects.get_or_create(user=request.user)
    
    return render(request, 'home.html', {'products': products, 'filter_form': filter_form, 'cart': cart})



@login_required
def user_products(request):
    products = Product.objects.filter(users=request.user)
    return render(request, 'user_products.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user not in product.users.all():
        return redirect('user_products')
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            if Product.objects.filter(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price']
            ).exists():
                messages.error(request, 'Product already exists.')
            else:
                form.save()
                return redirect('user_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user in product.users.all():
        product.delete()
    return redirect('user_products')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # If the product already exists, increment its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('home')
@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
    }
    return render(request, 'cart.html', context)

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart_item.quantity = int(quantity)
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')


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
