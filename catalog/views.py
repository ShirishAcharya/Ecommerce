from django.shortcuts import render,redirect
from catalog.models import Category,Product
from catalog.forms import ProductForm,SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.'

@login_required(login_url="/login/")
def home(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products}) 

def user_signup(request):
    if request.method=="POST":
        print(request.POST)
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=SignUpForm()
    return render(request, 'signup.html',{'form': form})

def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login/')


def create_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog/create/product/')
    else:
        form=ProductForm()
    return render(request,'create_product.html',{'form':form})

def list_product(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog/create/product/')
    else:
        form=ProductForm(instance=product)
    return render(request,'create_product.html',{'form':form})