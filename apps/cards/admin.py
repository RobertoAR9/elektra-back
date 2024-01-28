"""Admin to Cards panel administration"""

# Libraries
from django.contrib import admin

# Modules
from apps.cards.models import Card, PropertiesCard


class PropertiesCardInline(admin.TabularInline):
    """PropertiesCardInline to show properties card in card admin"""

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
    """CardAdmin to show cards in admin panel"""
    
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
