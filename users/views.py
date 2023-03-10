from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginUser(request):

    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist',extra_tags='danger')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Username OR password is incorrect',extra_tags='danger')

    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'User was logged out')
    return redirect('login')

def registerUser(request):
    form = CustomUserCreationForm()
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,'User account was created')

            login(request,user)
            return redirect('dashboard')
        else:
            messages.success(request,'An error has occurred during registration',extra_tags='danger')

    context = {'form':form}
    return render(request,'users/register.html',context)