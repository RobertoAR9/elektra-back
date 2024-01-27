from django.contrib import admin
from apps.cards.models import Card, PropertiesCard


class PropertiesCardInline(admin.TabularInline):
    """ PropertiesCardInline """

    model = PropertiesCard
    fields = (
        "balance",
        "amount",
        "expiration_date",
        "expiration_active",
        "restriction",
        "multiple_use",
        "transmitter",
        "type",
    )
    extra = 0
    min_num = 0
    can_delete = False
    show_change_link = False


class CardAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "clabe",
        "paid_card",
        "created_at",
    )
    inlines = [PropertiesCardInline]
    search_fields = ("email", "clabe")
    list_filter = ("email", "clabe")


admin.site.register(Card, CardAdmin)
