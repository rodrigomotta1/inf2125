import threading

from django.apps import AppConfig

from movrio.utils import generate_debug_estimates

class VisualizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visualizer'

    # def ready(self):
    #     """
    #     Inicia a thread da rotina de debug quando o Django inicia.
    #     """
    #     if not threading.main_thread().is_alive():
    #         return  # Evita rodar em processos paralelos como migrations

    #     thread = threading.Thread(target=generate_debug_estimates, daemon=True)
    #     thread.start()
