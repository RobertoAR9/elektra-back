# Create your models here.
from django.utils import timezone
from djongo import models
from django.utils.translation import gettext_lazy as _


TYPE = (
    ("Física", "Física"),
    ("Digital", "Digital"),
)

TRANSMITTER = (
    ("Sucursal", "Sucursal"),
    ("Línea", "Línea"),
)


class Card(models.Model):
    email = models.EmailField(max_length=100)
    clabe = models.CharField(max_length=100)
    paid_card = models.BooleanField(default=False)
    card_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Set verbose names"""

        verbose_name = _("Card")
        verbose_name_plural = _("Cards")
        ordering = ("-created_at",)

    def __str__(self):
        return self.clabe


class PropertiesCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = models.CharField(max_length=100, null=True)
    transmitter = models.CharField(max_length=100, choices=TRANSMITTER, null=True)
    type = models.CharField(max_length=100, choices=TYPE, null=True)
    expiration_active = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(default=timezone.now)
    restriction = models.BooleanField(default=False, null=True)
    multiple_use = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Set verbose names"""
            
        verbose_name = _("PropertiesCard")
        verbose_name_plural = _("PropertiesCards")
        ordering = ("-created_at",)

