from .forms import UserCreateForm
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import UserAuthenticateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupView(request):

    if request.method == 'GET':
        context = {
            'form': UserCreateForm
        }
        return render(request, 'accounts/signup.html', context)
    else:
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if password1 == password2:
            try:
                user = User.objects.create_user(username, password=password1)
                user.save()
                login(request, user)
                return redirect('movie:home')
            except IntegrityError:
                return render(request,
                 'accounts/signup.html', 
                {'form':UserCreateForm,
                 'error':'Username already exist. Try a New One'})
                
        else:
            return render(request, 'accounts/signup.html',
            {'form':UserCreateForm,
            'error':'Passwords do not match'})



def loginView(request):
    if request.method == 'GET':
        context = {
            'form': UserAuthenticateForm
        }
        return render(request, 'accounts/login.html',context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                 'form': UserAuthenticateForm,
                 'error': 'Username and password does not match'
            }
            return render(request, 'accounts/login.html',context)
        else:
            login(request, user)
            return redirect('movie:home')


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('movie:home')










