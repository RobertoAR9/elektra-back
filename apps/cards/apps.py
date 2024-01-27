from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "apps.cards"
    verbose_name = _("Cards")
