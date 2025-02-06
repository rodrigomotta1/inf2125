from django.core.management.base import BaseCommand
from visualizer.models import ThirdPartyInformation, VideoInformation, ImageInformation

class Command(BaseCommand):
    help = "Deleta todas as informações do banco de dados"

    def handle(self, *args, **kwargs):
        third_party_count = ThirdPartyInformation.objects.count()
        video_count = VideoInformation.objects.count()
        image_count = ImageInformation.objects.count()

        ThirdPartyInformation.objects.all().delete()
        VideoInformation.objects.all().delete()
        ImageInformation.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(
            f"Deletadas {third_party_count} informações de terceiros, {video_count} vídeos e {image_count} imagens."
        ))
