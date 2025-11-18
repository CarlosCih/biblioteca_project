from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegisterForm

def register(request):
    if request.method == 'POST':
        # Aquí iría la lógica para manejar el formulario de registro
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Se establece un usuario por defecto al grupo 'Usuarios
            grupo_usuario, _= Group.objects.get_or_create(name='Usuario')
            user.groups.add(grupo_usuario)

            #mensaje de exito
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('inicio_sesion:login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegisterForm()
    return render(request, 'inicio_sesion/session/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('biblioteca:index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'session/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio_sesion:login')

@login_required
def profile(request):
    return render(request, 'session/profile.html')

@login_required
def edit_profile(request):
    return render(request, 'session/edit_profile.html')