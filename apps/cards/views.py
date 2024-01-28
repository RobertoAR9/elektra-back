"""Module for Card views"""

# Libraries
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Modules
from apps.cards.models import Card
from apps.cards.serializers import CardSerializer


class CardView(APIView):
    """CardView create object card"""
    
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        email = data.pop("email")
        clabe = data.pop("clabe")
        properties = data.get("properties")
        expiration = properties.get("expiration_date")
        if expiration:
            activate_expiration = True
            properties.update({"expiration_active": activate_expiration})
        card = Card.objects.create(email=email, clabe=clabe)
        card.propertiescard_set.create(**properties)
        return Response(status=status.HTTP_201_CREATED)
    

class CardDetailView(APIView):
    """CardDetailView get object card and update paid_card"""

    permission_classes = [permissions.IsAuthenticated]

    def get(sel, request, pk):
        try:
            card_obj = Card.objects.get(pk=pk)
            cards = CardSerializer(card_obj).data
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(cards, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            card_obj = Card.objects.filter(id=pk).first()
            card_obj.paid_card = True
            card_obj.save()
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
