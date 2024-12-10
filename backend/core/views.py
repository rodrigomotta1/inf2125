from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Usuario, Local, Aviso, Informacao, Previsao
from core.serializers import UsuarioSerializer, LocalSerializer, AvisoSerializer, InformacaoSerializer, PrevisaoSerializer
from forecast.model_factory import FactoryModeloDePrevisao

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

    @action(detail=True, methods=['get'])
    def avisos(self, request, pk=None):
        local = self.get_object()
        avisos = local.avisos.all()
        serializer = AvisoSerializer(avisos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def informacoes(self, request, pk=None):
        local = self.get_object()
        informacoes = local.informacoes.all()
        serializer = InformacaoSerializer(informacoes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def previsoes(self, request, pk=None):
        local = self.get_object()
        previsoes = local.previsao_set.all()
        serializer = PrevisaoSerializer(previsoes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def previsao(self, request, pk=None):
        modelo_nome = request.query_params.get('modelo')
        if not modelo_nome:
            return Response({"error": "Modelo não especificado"}, status=status.HTTP_400_BAD_REQUEST)
        
        local = self.get_object()
        modelo = FactoryModeloDePrevisao.gerar_modelo(modelo_nome)
        estimativa = local.estimar(modelo)
        return Response({"estimativa": estimativa})

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def locais_favoritos(self, request):
        usuario = request.user.usuario
        locais = usuario.locais_favoritos.all()
        serializer = LocalSerializer(locais, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def adicionar_local(self, request):
        usuario = request.user.usuario
        local_id = request.data.get('local_id')
        try:
            local = Local.objects.get(pk=local_id)
        except Local.DoesNotExist:
            return Response({"error": "Local não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        usuario.locais_favoritos.add(local)
        return Response({"message": "Local adicionado aos favoritos"})

    @action(detail=True, methods=['delete'])
    def remover_local(self, request, pk=None):
        usuario = request.user.usuario
        try:
            local = Local.objects.get(pk=pk)
        except Local.DoesNotExist:
            return Response({"error": "Local não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        usuario.locais_favoritos.remove(local)
        return Response({"message": "Local removido dos favoritos"})

class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer

class InformacaoViewSet(viewsets.ModelViewSet):
    queryset = Informacao.objects.all()
    serializer_class = InformacaoSerializer

class PrevisaoViewSet(viewsets.ModelViewSet):
    queryset = Previsao.objects.all()
    serializer_class = PrevisaoSerializer
