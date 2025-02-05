import threading
import time
import random
from datetime import datetime, timedelta

from django.utils.timezone import make_aware
from django.apps import apps
from django.core.mail import send_mail

from movrio.interfaces.singleton import Singleton


class DatabaseQueryManager(Singleton):
    """
    Classe Singleton responsável por consultas ao banco de dados.
    """
    def get_all_places(self):
        """ Retorna todos os lugares cadastrados no sistema """
        from visualizer.models import Place
        return Place.objects.all()

    def get_place_by_id(self, place_id):
        """ Retorna um local específico pelo ID """
        from visualizer.models import Place
        return Place.objects.filter(id=place_id).first()

    def get_latest_estimates(self):
        """ Retorna as estimativas mais recentes de cada local """
        from visualizer.models import Estimate
        return Estimate.objects.order_by("-datetime")[:10]

    def get_user_saved_places(self, user):
        """ Retorna os lugares salvos pelo usuário """
        if user.is_authenticated:
            return user.userprofile.saved_places.all()
        return []


def send_email_notification(user_profile, message):
    """
    Deliver email notifcation to given user_profile object (from visualizer.models.UserProfile class) with given message
    """
    # send_mail(
    #     subject="Atualização em um local salvo",
    #     message=message,
    #     from_email="notificacoes@meusistema.com",
    #     recipient_list=[user_profile.user.email],
    # )
    
    print(f"Notificação para {user_profile.user.username} ({user_profile.user.email}): {message}")

def generate_debug_estimates():
    """
    Gera estimativas automaticamente a cada 10 segundos para todos os locais da base.
    - Se um local já tem estimativas, gera uma nova +30 minutos após a última.
    - Se um local não tem estimativas, gera uma estimativa para o momento atual.
    """

    while True:
        time.sleep(10)  # 🔹 Roda a cada 10 segundos

        # Obtém os modelos dinamicamente (evita importação circular)
        Place = apps.get_model("visualizer", "Place")
        Estimate = apps.get_model("visualizer", "Estimate")

        # Obtém todos os locais cadastrados
        places = Place.objects.all()

        for place in places:
            # Obtém a última estimativa do local (se existir)
            last_estimate = Estimate.objects.filter(place=place).order_by("-datetime").first()

            if last_estimate:
                next_estimate_time = last_estimate.datetime + timedelta(minutes=30) # type: ignore
            else:
                next_estimate_time = make_aware(datetime.now())

            # Gera uma estimativa aleatória
            estimate_amount = random.randint(10, 500)

            # Cria a nova estimativa
            Estimate.objects.create(
                place=place,
                datetime=next_estimate_time,
                amount=estimate_amount
            )

            print(f"[DEBUG] Criada estimativa para {place.name} às {next_estimate_time}: {estimate_amount} pessoas") # type: ignore

        print(f"[DEBUG] Atualizadas estimativas para {len(places)} locais.")