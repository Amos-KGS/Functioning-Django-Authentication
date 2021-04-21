from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . forms import SignupForm

# Create your views here.
def index(response):
    return render(response, "authentication/base.html", {})

def signup(response):
    form = SignupForm()
    return render(response, "authentication/signup.html", {"form":form})

def login(response):
    form = UserCreationForm()
    return render(response, "registration/login.html", {"form":form})


