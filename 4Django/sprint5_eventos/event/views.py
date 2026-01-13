from django.shortcuts import redirect, render
from .models import Evento
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm  ##
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout ##
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home (request):
    productos=Evento.objects.filter(estado=True)
    return render(request,'index.html',{'productos':productos})

#se requiere una instancia del formulario
def do_signup(request): 
    if request.method == 'POST':
        sign_up_form=SignUpForm(request.POST)
        if sign_up_form.is_valid() :
            username=sign_up_form.cleaned_data.get('username')  #cleaned para obtener.. idk
            nombres=sign_up_form.cleaned_data.get('nombres') 
            apellidos=sign_up_form.cleaned_data.get('apellidos') 
            email=sign_up_form.cleaned_data.get('email') 
            password=sign_up_form.cleaned_data.get('password') 

            if User.objects.filter(username=username).exists(): #validando q el usuario no exista
                messages.error(request, 'Usuario existente!')  #este msg se muestra en el bootstrap_messages
            else:
                #instancia del usuario
                nuevo_usuario=User(
                    username=username,
                    password=make_password(password),   #ofrece cifrado SHA256 por defecto
                    first_name=nombres,
                    last_name=apellidos,
                    email=email,
                    date_joined=datetime.now()
                )
                nuevo_usuario.save() #guardar usuario
                messages.success(request, '¡Registro exitoso!')
                # return redirect('home')
            
        
    else:
        sign_up_form=SignUpForm()

   
    
    return render(request, 'signup.html',{'form': sign_up_form})


def do_login(request):
    #generar sesion de usuario
    if request.method=='POST':
        auth_form=AuthenticationForm(request,data=request.POST) #recupera el usuario y contraseña
        if auth_form.is_valid():
            username=auth_form.cleaned_data.get('username')  
            password=auth_form.cleaned_data.get('password') 

            #valido que el user sea con esa password
            user=authenticate(username=username, password=password)
            if user is not None: ##si conincide
                login(request, user) ##el usuario tiene una sesion abierta
                messages.success(request, 'Inicio de sesión exitoso!')

                return render(request, 'index.html', {'username': username})
            else:
                messages.error(request, 'Usuario o contraseña invalidos!')

        else:
            messages.error(request, 'Usuario o contraseña invalidos!')
    else: ##si viene por get
        auth_form=AuthenticationForm()

    return render(request, 'login.html',{'login_form': auth_form})


def do_logout(request):
    logout(request)
    return redirect('home')