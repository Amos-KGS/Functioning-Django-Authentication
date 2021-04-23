from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . forms import SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(response):
    return render(response, "authentication/base.html", {})

def signup(response):
    if response.method == 'POST':
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(response, f'Your Account has been created successfully. Login to access your Acount')
            return redirect('login')
    else:    
        form = SignupForm()
            
    return render(response, "authentication/signup.html", {"form":form})

@login_required # adds functionality to underlying functions
def profile(request):
    return render(request, "authentication/profile.html")

