"""Serializers for cards app"""

# Libraries
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

# Modules
from apps.cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    """CardSerializer return data card"""
    class Meta:
        model = Card
        fields = "__all__"
