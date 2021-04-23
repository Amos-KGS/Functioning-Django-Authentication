from django.shortcuts import render
from . models import blogs

# Create your views here.

def index(request):
    post = {
        'blogss': blogs.objects.all()
    }
    return render(request, 'blogging/index.html', post)