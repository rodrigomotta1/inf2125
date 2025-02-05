import random
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand
from visualizer.models import Place, Estimate

class Command(BaseCommand):
    help = "Gera estimativas para todos os lugares, seguindo lógica de +30 min após a última estimativa"

    def handle(self, *args, **kwargs):
        places = Place.objects.all()
        created_count = 0

        for place in places:
            last_estimate = Estimate.objects.filter(place=place).order_by("-datetime").first()

            if last_estimate:
                next_estimate_time = last_estimate.datetime + timedelta(minutes=30)
            else:
                next_estimate_time = make_aware(datetime.now())

            estimate_amount = random.randint(10, 500)  # Gera um número aleatório de pessoas

            Estimate.objects.create(
                place=place,
                datetime=next_estimate_time,
                amount=estimate_amount
            )
            created_count += 1
            # self.stdout.write(f"[OK] Estimativa criada para {place.name} às {next_estimate_time}: {estimate_amount} pessoas")

        self.stdout.write(self.style.SUCCESS(f"Sucesso! {created_count} estimativas geradas."))