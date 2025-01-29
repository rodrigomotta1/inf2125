from django.core.mail import send_mail


def send_email_notification(user_profile, message):
    """
    Deliver email notifcation to given user_profile object (from visualizer.models.UserProfile class) with given message
    """
    print(f"Notificação para {user_profile.user.username} ({user_profile.user.email}): {message}")
    # send_mail(
    #     subject="Atualização em um local salvo",
    #     message=message,
    #     from_email="notificacoes@meusistema.com",
    #     recipient_list=[user_profile.user.email],
    # )