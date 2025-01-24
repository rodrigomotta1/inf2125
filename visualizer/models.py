from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, URLValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Place(models.Model):
    """
    TODO: Signals arch to notify Users when estimations changed; Methods to access specifics of a place
    """
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

    type_ = models.CharField(max_length=6, choices=PlaceType, default=PlaceType.BAIRRO, db_column="type")
    status = models.CharField(max_length=2, choices=StatusType)
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Estimate(models.Model):
    """
    NOTE: Always use datetime.datetime instances to set value of datetime:models.DateTimeField attribute
    """
    datetime = models.DateTimeField()

    amount = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="estimates")

    # estimation_model = ?

    def clean(self):
        """
        Include Estimate model pre-validation methods.
        This is applied before saving any instance of this class.
        """
        super().clean()
        current_datetime = now()

        # Check if Estimate instance is for the present or the future not the past
        if self.datetime and self.datetime < current_datetime:
            raise ValidationError(f"datetime: A data de estimativa não pode ser anterior a data atual ({current_datetime})")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Data: {self.datetime}, Quant.: {self.amount}"



class UserProfile(models.Model):
    """
    Core User attributes belongs to default User model from Django
    User attributes that are "profile" related (such as notification enabling choice) must be in this class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=False)

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
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="informations")

    class Meta:
        abstract = True



class ThirdPartyInformation(Information):
    """
    Information entities that come from third party sources, often already verified (such as city sources)
    """
    source_name = models.TextField()
    source_url = models.TextField(validators=[
        URLValidator(verify_exists=True)
    ])


class ImageInformation(Information):
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class VideoInformation(Information):
    video_url = models.TextField(validators=[
        URLValidator(verify_exists=True)
    ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)