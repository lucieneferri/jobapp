from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    context={}
    return render(request, 'login_register.html', context)

def home(request):
    return render(request, 'home.html')

