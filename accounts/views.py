from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})

def userlogin(request): #login은 함수명과 똑같아서 안 됨
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도해보세요')

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def userlogout(request):
    logout(request)
    return  HttpResponseRedirect('/')