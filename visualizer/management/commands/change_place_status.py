import random
from django.core.management.base import BaseCommand
from visualizer.models import Place, UserProfile

class Command(BaseCommand):
    help = "Modifica o status de um Place aleatório salvo pelo admin"

    def handle(self, *args, **kwargs):
        """
        Modifica aleatoriamente o status de um Place salvo pelo admin.
        """
        # Busca um usuário admin
        user = UserProfile.objects.filter(pk=1).first()

        # Busca um Place aleatório salvo pelo admin
        saved_places = user.saved_places.all() # type: ignore

        if not saved_places.exists():
            self.stdout.write(self.style.ERROR("Nenhum Place salvo pelo admin."))
            return

        place = random.choice(saved_places)
        
        # Modifica o status usando o método change_status()
        old_status = place.status
        options = list(Place.StatusType)
        options.remove(old_status)

        new_status = random.choice(options)

        place.change_status(new_status)

        self.stdout.write(self.style.SUCCESS(
            f"Status de '{place.name}' alterado de {old_status} para {new_status}."
        ))
