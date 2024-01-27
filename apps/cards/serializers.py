from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"