from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib import messages

User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Неверные учетные данные')
            return render(request, 'custom_auth/login.html')
    
    return render(request, 'custom_auth/login.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                auth_login(request, user)  
                return redirect('home') 
            except Exception as e:
                return render(request, 'custom_auth/reg.html', {'error': str(e)})
        else:
            return render(request, 'custom_auth/reg.html', {'error': 'Пароли не совпадают'})
    return render(request, 'custom_auth/reg.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  