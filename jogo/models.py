from django.db import models
from usuarios.models import Usuario

class Mapa(models.Model):
    nome = models.CharField(max_length=100)
    layout = models.JSONField()  # guarda a matriz do mapa em JSON

class Partida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    posicao = models.JSONField(default=dict)  # posição atual do personagem
    concluido = models.BooleanField(default=False)
