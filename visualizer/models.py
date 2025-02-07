from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, URLValidator

from movrio.interfaces.observer import Observer, Publisher
from movrio.utils import send_email_notification


class Place(models.Model, Publisher):
    class PlaceType(models.TextChoices):
        RUA = "RUA", "Rua"
        PRAIA = "PRAIA", "Praia"
        BAIRRO = "BAIRRO", "Bairro"
        PONTO_TURISTICO = "PT_TUR", "Ponto Turístico"
        PRACA = "PRACA", "Praça"
    class StatusType(models.TextChoices):
        POUCO_MOVIMENTADO = "PM", "Pouco movimentado"
        MOVIMENTACAO_INTENSA = "MI", "Movimentação intensa"
        MUITO_MOVIMENTADO = "MM", "Muito movimentado"

    type = models.CharField(max_length=6, choices=PlaceType, default=PlaceType.BAIRRO, db_column="type")
    status = models.CharField(max_length=2, choices=StatusType)
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()

    observers = models.ManyToManyField('UserProfile', related_name="saved_places")

    def add_observer(self, observer: Observer):
        self.observers.add(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self, event_data):
        for observer in self.observers.all():
            print(observer)
            observer.update(event_data)

    def change_status(self, new_status: str):
        self.status = new_status
        self.save()
        self.notify_observers({
            'place': self.name,
            'status': new_status
        })

    def get_trend_icon(self) -> str:
        """
        Retorna o ícone de tendência baseado nas últimas estimativas do local.
        """
        estimates = self.estimates.order_by("-datetime")[:2]  # Pega as duas últimas estimativas

        if len(estimates) < 2:
            return "ti ti-minus"  # Sem dados suficientes para comparar

        latest_estimate = estimates[0].amount
        second_latest_estimate = estimates[1].amount

        if latest_estimate > second_latest_estimate:
            return "ti ti-trending-up"
        elif latest_estimate < second_latest_estimate:
            return "ti ti-trending-down"
        else:
            return "ti ti-minus"

    def get_status_display(self):
        """
        Retorna o nome por extenso do status.
        """
        if self.status == "PM":
            return "Pouco movimentado"
        elif self.status == "MI":
            return "Movimentação intensa"
        elif self.status == "MM":
            return "Muito movimentado"
                
    def __str__(self):
        return self.name


class Estimate(models.Model):
    """
    NOTE: Always use datetime.datetime instances to set value of datetime:models.DateTimeField attribute
    """
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="estimates")
    datetime = models.DateTimeField()
    amount = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    def save(self, *args, **kwargs):
        """
        Atualiza o status da instância de Place ao salvar um novo Estimate recente.
        """
        super().save(*args, **kwargs)  # Salva a instância primeiro

        # Verifica se o estimate foi criado recentemente (dentro de 5 minutos do tempo atual)
        if abs((self.datetime - now()).total_seconds()) <= 300:
            if self.amount <= 150:
                self.place.change_status(Place.StatusType.POUCO_MOVIMENTADO)
            elif 151 <= self.amount <= 300:
                self.place.change_status(Place.StatusType.MOVIMENTACAO_INTENSA)
            else:
                self.place.change_status(Place.StatusType.MUITO_MOVIMENTADO)

    def __str__(self):
        return f"{self.datetime.strftime('%d/%m/%Y')} às {self.datetime.strftime('%H:%M')}: {self.amount} pessoas"



class UserProfile(models.Model, Observer):
    """
    Core User attributes belongs to default User model from Django
    User attributes that are "profile" related (such as notification enabling choice) must be in this class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=False)

    def update(self, event_data):
        if self.notifications_enabled:
            send_email_notification(self, f"O status de {event_data['place']} mudou para {event_data['status']}")

    def __str__(self):
        return self.user.username


class Information(models.Model):
    """
    Abstract Base Model for Information related classes
    Used to differ different types of Information (video, image, official info and so on)
    """
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)

    place = models.ForeignKey(
        Place, 
        on_delete=models.CASCADE, 
        related_name="%(app_label)s_%(class)s_related", 
        related_query_name="%(app_label)s_%(class)ss"
    )

    class Meta:
        abstract = True



class ThirdPartyInformation(Information):
    """
    Information entities that come from third party sources, often already verified (such as city sources)
    """
    source_name = models.TextField()
    source_url = models.TextField(validators=[
        URLValidator()
    ])


class ImageInformation(Information):
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class VideoInformation(Information):
    video_url = models.TextField(validators=[
        URLValidator()
    ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)