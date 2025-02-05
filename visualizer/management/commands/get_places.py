import requests
from django.core.management.base import BaseCommand
from visualizer.models import Place

class Command(BaseCommand):
    help = "Carrega latitude e longitude de todos os bairros oficiais do Rio de Janeiro e os adiciona ao banco"

    API_URL = "https://nominatim.openstreetmap.org/search"

    BAIRROS = [
        "Abolição", "Acari", "Água Santa", "Alto da Boa Vista", "Anchieta", "Andaraí", "Anil", "Bancários", "Bangu",
        "Barra da Tijuca", "Barra de Guaratiba", "Barros Filho", "Benfica", "Bento Ribeiro", "Bonsucesso", "Botafogo",
        "Brás de Pina", "Cachambi", "Cacuia", "Caju", "Camorim", "Campinho", "Campo dos Afonsos", "Campo Grande",
        "Cascadura", "Catete", "Catumbi", "Cavalcanti", "Centro", "Cidade de Deus", "Cidade Nova", "Cidade Universitária",
        "Cocotá", "Coelho Neto", "Colégio", "Complexo do Alemão", "Copacabana", "Cordovil", "Cosme Velho", "Cosmos",
        "Costa Barros", "Curicica", "Del Castilho", "Deodoro", "Encantado", "Engenheiro Leal", "Engenho da Rainha",
        "Engenho de Dentro", "Engenho Novo", "Estácio", "Flamengo", "Freguesia", "Freguesia (Jacarepaguá)", "Galeão",
        "Gamboa", "Gardênia Azul", "Gávea", "Gericinó", "Glória", "Grajaú", "Grumari", "Guadalupe", "Guaratiba",
        "Higienópolis", "Honório Gurgel", "Humaitá", "Inhaúma", "Inhoaíba", "Ipanema", "Irajá", "Itanhangá", "Jacaré",
        "Jacarepaguá", "Jacarezinho", "Jardim América", "Jardim Botânico", "Jardim Carioca", "Jardim Guanabara",
        "Jardim Sulacap", "Joá", "Lagoa", "Laranjeiras", "Leblon", "Leme", "Lins de Vasconcelos", "Madureira",
        "Magalhães Bastos", "Mangueira", "Manguinhos", "Maracanã", "Maré", "Marechal Hermes", "Maria da Graça", "Méier",
        "Moneró", "Olaria", "Oswaldo Cruz", "Paciência", "Padre Miguel", "Paquetá", "Parada de Lucas", "Parque Anchieta",
        "Parque Colúmbia", "Pavuna", "Pechincha", "Pedra de Guaratiba", "Penha", "Penha Circular", "Piedade", "Pilares",
        "Pitangueiras", "Portuguesa", "Praça da Bandeira", "Praça Seca", "Praia da Bandeira", "Quintino Bocaiúva",
        "Ramos", "Realengo", "Recreio dos Bandeirantes", "Riachuelo", "Ribeira", "Ricardo de Albuquerque", "Rio Comprido",
        "Rocha", "Rocha Miranda", "Rocinha", "Sampaio", "Santa Cruz", "Santa Teresa", "Santíssimo", "Santo Cristo",
        "São Conrado", "São Cristóvão", "São Francisco Xavier", "Saúde", "Senador Camará", "Senador Vasconcelos",
        "Sepetiba", "Tanque", "Taquara", "Tauá", "Tijuca", "Todos os Santos", "Tomás Coelho", "Turiaçu", "Urca",
        "Vargem Grande", "Vargem Pequena", "Vasco da Gama", "Vaz Lobo", "Vicente de Carvalho", "Vidigal", "Vigário Geral",
        "Vila da Penha", "Vila Isabel", "Vila Kosmos", "Vila Militar", "Vila Valqueire", "Vista Alegre", "Zumbi"
    ]

    def handle(self, *args, **kwargs):
        created_count = 0
        new_places = []

        for bairro in self.BAIRROS:
            if Place.objects.filter(name=bairro).exists():
                # self.stdout.write(f"[SKIP] {bairro} já existe no banco de dados.")
                break

            new_places.append(bairro)

            params = {
                "q": f"{bairro}, Rio de Janeiro, Brasil",
                "format": "json",
                "limit": 1
            }

            try:
                response = requests.get(self.API_URL, params=params, timeout=5)
                response.raise_for_status()  # Verifica erros HTTP
                data = response.json()

                if not data:
                    self.stdout.write(self.style.WARNING(f"[ERRO] Coordenadas não encontradas para {bairro}."))
                    continue

                latitude = float(data[0]["lat"])
                longitude = float(data[0]["lon"])

                Place.objects.create(
                    name=bairro,
                    latitude=latitude,
                    longitude=longitude,
                    type=Place.PlaceType.BAIRRO,
                    status=Place.StatusType.POUCO_MOVIMENTADO
                )

                created_count += 1
                # self.stdout.write(f"[OK] {bairro} cadastrado com lat: {latitude}, lon: {longitude}")

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"[ERRO] Falha ao obter dados para {bairro}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Sucesso! {created_count} bairros adicionados ao banco de dados."))
