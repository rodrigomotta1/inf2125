from django.core.management.base import BaseCommand
from visualizer.models import Place

class Command(BaseCommand):
    help = "Remove todos os locais do banco de dados"

    def handle(self, *args, **kwargs):
        count, _ = Place.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Sucesso! {count} locais foram removidos do sistema."))
