from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.username.POST.get('username')
        password = request.password.POST.get('password')

        try: #ter certeza que o usuário existe no banco de dados
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User or Password does not exist')

        user = authenticate(request, username=username, password=password)
        #ou ele joga um erro, ou retorna um objeto do usuário que combine com essas credenciais

        if user is not None:
            login(request, user) #login adiciona a sessão para o usuário no banco de dados e no navegador
            return redirect('home')

        else:
            messages.error(request, 'Username or Password does not exist')








    context={}
    return render(request, 'login_register.html', context)

def home(request):
    return render(request, 'home.html')

