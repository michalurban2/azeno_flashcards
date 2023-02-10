from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FlashCard
from .serializers import FlashCardSerializer

class FashCardsView(ListCreateAPIView):
    # queryset = FlashCard.objects.filter(rating__gte=42)
    permission_classes = [IsAuthenticated]
    serializer_class = FlashCardSerializer

    # queryset = FlashCard.objects.all()

    def get_queryset(self):
        rating = self.request.query_params.get('rating', 0)
        return FlashCard.objects.filter(rating__gte=rating)


class FlashCardItemAsView(RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
