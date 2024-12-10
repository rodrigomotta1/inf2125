from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from forecast.forecast_models import ModeloDePrevisao  # Importar a classe abstrata de previsão
from datetime import datetime
from django.contrib.auth.models import User


class Aviso(models.Model):
    descricao = models.TextField()  # Descrição do aviso
    tipo = models.CharField(max_length=50)  # Tipo de aviso (e.g., 'segurança', 'climático')
    fonte = models.CharField(max_length=100)  # Fonte do aviso (e.g., 'Prefeitura', 'API externa')
    data = models.DateField()  # Data do aviso

    def __str__(self):
        return f"{self.tipo}: {self.descricao[:30]}..."  # Representação com o tipo e início da descrição


class Local(models.Model):
    nome = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    avisos = models.ManyToManyField(
        Aviso,  # Relaciona com a classe Aviso
        related_name='locais',  # Permite acessar os locais relacionados a um aviso
        blank=True  # Permite que um local não tenha avisos associados inicialmente
    )

    informacoes = models.ManyToManyField('Informacao', related_name='locais', blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'latitude', 'longitude'],
                name="unique_nome_latitude_longitude"
            )
        ]

    def estimar(self, modelo: ModeloDePrevisao):
        """
        Realiza a estimativa para este local usando o modelo fornecido.
        Considera as informações e avisos mais recentes associados a este local.
        :param modelo: Instância de um modelo de previsão que herda de ModeloDePrevisao.
        :return: Resultado da estimativa.
        """
        # Obter as informações mais recentes relacionadas ao local
        informacoes = self.informacoes.order_by('-id')  # Informações mais recentes

        # Obter os avisos mais recentes relacionados ao local
        avisos = self.avisos.order_by('-id')  # Avisos mais recentes

        # Preparar os dados de entrada para o modelo
        dados_entrada = {
            "informacoes": list(informacoes.values('tipo', 'descricao')),
            "avisos": list(avisos.values('tipo', 'descricao', 'data')),
            "latitude": float(self.latitude),
            "longitude": float(self.longitude),
            "data_hora": datetime.now().isoformat(),
        }

        # Realizar a estimativa usando o modelo fornecido
        try:
            estimativa = modelo.processar(dados_entrada)
        except Exception as e:
            raise ValueError(f"Erro ao processar o modelo: {e}")

        return estimativa

    def __str__(self):
        return self.nome


class Previsao(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    estimativa_pessoas = models.PositiveIntegerField()
    modelo = models.CharField(max_length=255)
    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE,
        related_name='previsoes'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['data', 'hora', 'modelo', 'local'],
                name="unique_data_hora_modelo_local"
            )
        ]

    def __str__(self):
        return f"Previsão para {self.local.nome} em {self.data} às {self.hora}"


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    locais_favoritos = models.ManyToManyField(
        Local,
        related_name="usuarios_favoritos",
        blank=True
    )

    def __str__(self) -> str:
        return self.user.username


class Informacao(models.Model):
    TIPO_CHOICES = [
        ('evento', 'Evento'),
        ('alerta', 'Alerta'),
        ('outro', 'Outro'),
    ]

    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="informacoes/", null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='informacoes')

    def __str__(self):
        return f"{self.tipo}: {self.descricao[:30]}..."  # Representação textual da informação