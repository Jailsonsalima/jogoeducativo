from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
            messages.success(request, "Conta criada com sucesso!")

        # autentica usuário
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect("jogo")  # vai para o jogo
        else:
            messages.error(request, "Erro ao autenticar usuário.")

    return render(request, "usuarios/login.html")
