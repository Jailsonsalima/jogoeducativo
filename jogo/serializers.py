from rest_framework import serializers

class ComandoSerializer(serializers.Serializer):
    comandos = serializers.ListField(
        child=serializers.CharField()
    )
