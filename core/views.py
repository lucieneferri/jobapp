from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
