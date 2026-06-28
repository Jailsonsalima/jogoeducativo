from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # tenta encontrar usuário pelo email
        user = User.objects.filter(username=email).first()

        if user is None:
            # cria usuário novo
            user = User.objects.create_user(username=email, email=email, password=senha)
            messages.success(request, "Conta criada com sucesso! Faça login para continuar.")

        # autentica usuário
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect("jogo")  # vai para o jogo
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)  # encerra a sessão
    messages.success(request, "Você saiu da sua conta com sucesso!")
    return redirect("home")  # volta para a página de login