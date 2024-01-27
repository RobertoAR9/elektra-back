from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.cards.models import Card
from apps.cards.serializers import CardSerializer

class CardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        expiration = data.get("expiration_date")
        if expiration:
            activate_expiration = True
            data.update({"expiration_active": activate_expiration})
        Card.objects.create(**data)
        return Response(status=status.HTTP_201_CREATED)
    

class CardDetailView(APIView):
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
            card_obj = Card.objects.get(pk=pk)
            balance = str(card_obj.balance)
            amount = str(card_obj.amount)
            card_obj.balance = float(balance)
            card_obj.amount = float(amount)
            card_obj.paid_card = True
            card_obj.save()
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
