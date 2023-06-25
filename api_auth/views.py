from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import *
from django.contrib import messages


# authenticating users
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def registerPage (request):
    if request.user.is_authenticated:
        return redirect('todos:todo_app')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('todos:home')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('todos:todo_app')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('todos:todo_app')
            else:
                messages.error(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'registration/login.html', context)
    
    
def logoutUser(request):
    logout(request)
    return redirect('todos:home')
