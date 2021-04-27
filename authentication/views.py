from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . forms import SignupForm, UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index(response):
    title = 'Home'
    return render(response, "authentication/home.html", {"title":title})

def signup(response):
    if response.method == 'POST':
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(response, f'Your Account has been created successfully. Login to access your Account')
            return redirect('login')
    else:    
        form = SignupForm()
            
    return render(response, "authentication/signup.html", {"form":form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True) # clears user cache hence disabling back-button from going back to previous page after user logs out
@login_required # adds functionality to underlying functions
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account update successful!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    ls = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, "authentication/profile.html", ls)

