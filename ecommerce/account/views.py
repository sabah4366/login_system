from django.shortcuts import render,redirect
from .forms import CreateUserForm
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('account:home')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'account/login.html',{})


    return render(request,'account/login.html',{})


@unauthenticated_user
def register_page(request):
    form =CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' +  user)
            return redirect('account:login')


    context={
        'form':form
    }
    return render(request,'account/register.html',context)

@login_required(login_url='account:login')
def logout_view(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='account:login')
def home_view(request):
    return render(request,'account/home.html',{})