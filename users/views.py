from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserUpdateForm
from django.contrib.auth import logout as auth_logout


def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        if User.objects.filter(username=username).exists():
            messages.error(request, f'{username} already exist !')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username,email=email,password=password)
       
        messages.success(request, f' {username} your account is created ')
      
        return redirect('login')
    return render(request,'register.html')


def user_logout(request):
    auth_logout(request)
    return redirect('homepage')
     
    