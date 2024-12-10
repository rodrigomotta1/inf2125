from rest_framework import serializers
from core.models import Usuario, Local, Aviso, Informacao, Previsao

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'

class InformacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacao
        fields = '__all__'

class PrevisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previsao
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    avisos = AvisoSerializer(many=True, read_only=True)
    informacoes = InformacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Local
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    locais_favoritos = LocalSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'
