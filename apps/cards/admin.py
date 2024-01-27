from django.contrib import admin
from apps.cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "clabe",
        "balance",
        "transmitter",
        "type",
        "expiration_active",
        "created_at",
    )
    search_fields = ("email", "clabe", "transmitter", "type")
    list_filter = ("email", "clabe", "transmitter", "type")


admin.site.register(Card, CardAdmin)
