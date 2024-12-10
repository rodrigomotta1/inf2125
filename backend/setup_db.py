"""
Script para populacao de dados mockup no banco
"""
import os
import django

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Usuario, Local, Aviso, Informacao, Previsao

def run():
    # Limpar os dados anteriores
    User.objects.all().delete()
    Local.objects.all().delete()
    Aviso.objects.all().delete()
    Informacao.objects.all().delete()
    Previsao.objects.all().delete()

    # Criar usuários
    user1 = User.objects.create_user(username="joao", email="joao@example.com", password="senha123")
    user2 = User.objects.create_user(username="maria", email="maria@example.com", password="senha123")

    # Criar perfis de usuários
    usuario1 = Usuario.objects.create(user=user1)
    usuario2 = Usuario.objects.create(user=user2)

    # Criar locais
    local1 = Local.objects.create(nome="Praia de Copacabana", latitude=-22.9711, longitude=-43.1822)
    local2 = Local.objects.create(nome="Praia de Ipanema", latitude=-22.9869, longitude=-43.2065)

    # Associar locais favoritos
    usuario1.locais_favoritos.add(local1, local2)
    usuario2.locais_favoritos.add(local2)

    # Criar avisos
    aviso1 = Aviso.objects.create(descricao="Risco de ressaca no mar.", tipo="climático", fonte="Prefeitura", data="2024-12-10")
    aviso2 = Aviso.objects.create(descricao="Evento público programado.", tipo="evento", fonte="Prefeitura", data="2024-12-12")
    local1.avisos.add(aviso1)
    local2.avisos.add(aviso2)

    # Criar informações
    informacao1 = Informacao.objects.create(tipo="alerta", descricao="Praia lotada, risco de aglomeração.", usuario=usuario1)
    informacao2 = Informacao.objects.create(tipo="evento", descricao="Competição de surfe acontecendo.", usuario=usuario2)
    local1.informacoes.add(informacao1)
    local2.informacoes.add(informacao2)

    # Criar previsões
    previsao1 = Previsao.objects.create(data="2024-12-15", hora="14:00:00", estimativa_pessoas=500, modelo="Modelo IA V1", local=local1)
    previsao2 = Previsao.objects.create(data="2024-12-16", hora="10:00:00", estimativa_pessoas=300, modelo="Modelo Histórico", local=local2)

    print("Banco de dados populado com sucesso!")


if __name__ == "__main__":
    run()
