from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index/home.html')

def login(request):
    return render(request, 'index/login.html')