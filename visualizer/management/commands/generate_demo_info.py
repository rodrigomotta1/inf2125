from django.core.management.base import BaseCommand
from django.utils.timezone import now
from visualizer.models import Place, ThirdPartyInformation, VideoInformation, ImageInformation, User
import random

class Command(BaseCommand):
    help = "Gera informações demonstrativas para todos os lugares no banco de dados"

    def handle(self, *args, **kwargs):
        places = Place.objects.all()
        user = User.objects.filter(id=1).first()

        if not places.exists():
            self.stdout.write(self.style.ERROR("Nenhum lugar encontrado no banco de dados."))
            return

        info_count = 0
        for place in places:
            # Criar uma informação de terceiros
            ThirdPartyInformation.objects.create(
                place=place,
                title="Fonte Oficial - Atualização",
                description=f"Nova atualização sobre {place.name}.",
                source_name="Prefeitura RJ",
                source_url="https://www.rio.rj.gov.br",
                created_at=now()
            )

            # Criar uma informação de vídeo
            VideoInformation.objects.create(
                place=place,
                title="Vídeo sobre o Local",
                description=f"Veja um vídeo sobre {place.name}.",
                video_url="https://www.youtube.com/watch?v=abcdef",
                created_at=now(),
                author=user
            )

            # Criar uma informação de imagem
            ImageInformation.objects.create(
                place=place,
                title="Foto Atualizada",
                description=f"Imagem recente de {place.name}.",
                image="default.jpg",  # Supondo uma imagem demonstrativa no sistema
                created_at=now(),
                author=user
            )

            info_count += 3  # Criamos três informações para cada lugar

        self.stdout.write(self.style.SUCCESS(f"{info_count} informações geradas com sucesso!"))
