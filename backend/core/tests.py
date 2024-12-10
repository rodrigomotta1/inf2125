from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Usuario, Local, Aviso, Informacao, Previsao
from forecast.model_factory import FactoryModeloDePrevisao

class ProjetoTestes(TestCase):
    def setUp(self):
        """
        Configuração inicial dos objetos para os testes.
        """
        # Criar usuários padrão do Django
        self.user1 = User.objects.create_user(username="joao", password="senha123")
        self.user2 = User.objects.create_user(username="maria", password="senha123")

        # Criar perfis de usuários
        self.usuario1 = Usuario.objects.create(user=self.user1)
        self.usuario2 = Usuario.objects.create(user=self.user2)

        # Criar um local
        self.local = Local.objects.create(nome="Praia de Copacabana", latitude=-22.9711, longitude=-43.1822)

        # Associar favoritos
        self.usuario1.locais_favoritos.add(self.local)

        # Criar avisos
        self.aviso1 = Aviso.objects.create(descricao="Risco de ressaca no mar.", tipo="climático", fonte="Prefeitura", data="2024-12-10")
        self.aviso2 = Aviso.objects.create(descricao="Evento público programado.", tipo="evento", fonte="Prefeitura", data="2024-12-12")

        # Criar informações
        self.informacao1 = Informacao.objects.create(tipo="alerta", descricao="Praia lotada, risco de aglomeração.", imagem=None, usuario=self.usuario1)
        self.informacao2 = Informacao.objects.create(tipo="evento", descricao="Competição de surfe acontecendo.", imagem=None, usuario=self.usuario2)

    def test_associacoes_usuario_local(self):
        """
        Testa as associações entre usuários e locais favoritos.
        """
        self.assertIn(self.local, self.usuario1.locais_favoritos.all())
        self.assertNotIn(self.local, self.usuario2.locais_favoritos.all())

    def test_associacoes_local_avisos_informacoes(self):
        """
        Testa as associações de avisos e informações com o local.
        """
        # Associar avisos ao local
        self.local.avisos.add(self.aviso1, self.aviso2)
        self.assertIn(self.aviso1, self.local.avisos.all())
        self.assertIn(self.aviso2, self.local.avisos.all())

        # Associar informações ao local
        self.local.informacoes.add(self.informacao1, self.informacao2)
        self.assertIn(self.informacao1, self.local.informacoes.all())
        self.assertIn(self.informacao2, self.local.informacoes.all())

    def test_modelo_de_previsao_imagem(self):
        """
        Testa a criação e utilização de um modelo de previsão baseado em imagem.
        """
        modelo_imagem = FactoryModeloDePrevisao.gerar_modelo("imagem", parametros={"resolucao": "alta"})
        estimativa = self.local.estimar(modelo_imagem)
        self.assertIsNotNone(estimativa)

    def test_modelo_de_previsao_serie(self):
        """
        Testa a criação e utilização de um modelo de previsão baseado em séries temporais.
        """
        modelo_serie = FactoryModeloDePrevisao.gerar_modelo("serie", parametros={"historico_dias": 30})
        estimativa = self.local.estimar(modelo_serie)
        self.assertIsNotNone(estimativa)

    def test_criacao_previsoes(self):
        """
        Testa a criação de previsões associadas ao local.
        """
        previsao1 = Previsao.objects.create(data="2024-12-15", hora="14:00:00", estimativa_pessoas=500, modelo="Modelo IA V1", local=self.local)
        previsao2 = Previsao.objects.create(data="2024-12-16", hora="10:00:00", estimativa_pessoas=300, modelo="Modelo Histórico", local=self.local)
        self.assertEqual(previsao1.local, self.local)
        self.assertEqual(previsao2.local, self.local)

    def test_factory_modelo_de_previsao(self):
        """
        Testa a fábrica de modelos de previsão.
        """
        modelo_imagem = FactoryModeloDePrevisao.gerar_modelo("imagem")
        self.assertIsInstance(modelo_imagem, FactoryModeloDePrevisao.gerar_modelo("imagem").__class__)

        modelo_serie = FactoryModeloDePrevisao.gerar_modelo("serie")
        self.assertIsInstance(modelo_serie, FactoryModeloDePrevisao.gerar_modelo("serie").__class__)

        with self.assertRaises(ValueError):
            FactoryModeloDePrevisao.gerar_modelo("desconhecido")
