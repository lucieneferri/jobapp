from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

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

    context={'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)#pega as infos de usuario e senha
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occour during registration')


    return render(request, 'login_register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

