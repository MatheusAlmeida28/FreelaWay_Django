from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from .utils import password_is_valid, user_success, sistema_erro, username_is_valid, user_is_not_valid
from django.contrib import auth

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/jobs/encontrar_jobs')      
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not username_is_valid(request, username):
            return redirect('/auth/cadastro')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,
                                                password=senha)
            user.save()
            user_success(request)
            return redirect('/auth/logar')
        
        except:
            sistema_erro(request)
            return redirect('/auth/cadastro')


        
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/jobs/encontrar_jobs') 
        return render(request, 'logar.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        
        usuario = auth.authenticate(username=username, password=senha)
    
  
        if not usuario:
            user_is_not_valid(request)
            return redirect('/auth/logar')
        
        else:
            auth.login(request, usuario)
            return redirect('/jobs/encontrar_jobs')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


#teste
