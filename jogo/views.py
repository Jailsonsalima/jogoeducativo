from django.shortcuts import render
from .models import Mapa
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ComandoSerializer
from .utils import executar_comandos

@login_required(login_url='/')
def jogo_view(request):
    mapa = Mapa.objects.first()  # pega um mapa de exemplo
    return render(request, "jogo/jogo.html", {"mapa": mapa})



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def executar_view(request):
    serializer = ComandoSerializer(data=request.data)
    if serializer.is_valid():
        comandos = serializer.validated_data["comandos"]
        resultado = executar_comandos(comandos)
        return Response(resultado)
    return Response(serializer.errors, status=400)
