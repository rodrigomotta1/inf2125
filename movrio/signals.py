"""
Signal handlers module
"""

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from visualizer.models import Place, UserProfile, User, Estimate
from .utils import send_email_notification

# Defines this function the signal handler for Place instances notification to User/UserProfile instances.
# `receiver` have as first argument the type of event that trigger this handler, and as second argument the observer
# audience, related to models. If None is given, then the hanlder reacts to any event on any model class.
@receiver(pre_save, sender=Place)
def notify_users_on_place_status_update(sender, instance, **kwargs):
    """
    Triggerd when Place.status changes
    """

    # Check if object exists in database
    if instance.pk:
        old_instance = Place.objects.filter(pk=instance.pk).first()

        # If old instance status is different of new instance status, status attribute has changed -> notify users
        if old_instance and old_instance.status != instance.status:
            user_profiles = instance.observers.all() # type: ignore
            for user_profile in user_profiles:
                if user_profile.notifications_enabled:
                    send_email_notification(
                        user_profile,
                        f"O status de {instance.name} mudou para {instance.get_status_display()}"
                    )


@receiver(post_save, sender=Estimate)
def notify_users_on_place_estimates_update(sender, instance, **kwargs):
    """
    Triggered when Place.estimates receives another object association
    """
    place = instance.place
    user_profiles = place.observers.all()

    for user_profile in user_profiles:
        if user_profile.notfications_enabled:
            send_email_notification(
                user_profile,
                f"Uma nova estimativa foi adicionada a {place.name}: {instance.amount} pessoas previstas para {instance.datetime.strftime('%d/%m/%Y às %H:%M')}"
            )


@receiver(post_save, sender=User)
def create_user_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)