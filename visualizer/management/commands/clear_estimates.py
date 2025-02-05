from django.core.management.base import BaseCommand
from visualizer.models import Estimate

class Command(BaseCommand):
    help = "Remove todas as estimativas do sistema"

    def handle(self, *args, **kwargs):
        count, _ = Estimate.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Sucesso! {count} estimativas foram removidas do sistema."))