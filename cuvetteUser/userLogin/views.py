from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def homepage(request):
    return render(request, 'userLogin/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")

    context = {'registerform':form}

    return render(request, 'userLogin/register.html', context=context)


def my_login(request):
    form = LoginForm()
    custom_error = None
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')

            user = authenticate(username=username_or_email,password=password)

            if user is None:
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username
                    user = authenticate(username=username,password=password)
                except:
                    user = None
                    custom_error = 'Invalid password or username. Please try again.'
             
            if user is not None:
                auth.login(request,user) 
                return redirect("dashboard")
    
    context = {'loginform': form,'Error': custom_error}
    return render(request, 'userLogin/my-login.html',context=context)

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'userLogin/dashboard.html',{'user': request.user})

def my_logout(request):
    auth.logout(request)
    return redirect("my-login")

@login_required(login_url="my-login")
def profile(request):
    return render(request,'userLogin/profile.html', {'user': request.user})
