from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def signup_view(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('/hospitals')
    else:
        form = UserCreationForm()
    return render(response, 'accounts/signup.html', {"form":form})

def login_view(response):
    if response.method == "POST":
        form = AuthenticationForm(data=response.POST)
        if form.is_valid():
            user = form.get_user()
            login(response, user)
            return redirect('/hospitals')
    else:
        form = AuthenticationForm()
    return render(response, 'accounts/login.html', {'form':form})

def logout_view(response):
    if response.method == "POST":
        logout(response)
        return redirect('/home')