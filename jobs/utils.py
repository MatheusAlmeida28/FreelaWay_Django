from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User

def user_exist(request):
    messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse Username')

def email_exist(request):
    messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse E-mail')

def dados_success(request):
    messages.add_message(request, constants.SUCCESS, 'Dados alterado com sucesso')