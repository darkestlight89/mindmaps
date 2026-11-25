from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def redirect_home(request):
    return redirect("/home")

def index(request):
    return render(request, 'index.html')

def load(request):
    return render(request, 'load.html')

def how_it_works(request):
    return render(request, 'how-it-works.html')