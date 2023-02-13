from django.core import paginator
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from . import models, serializers
from .permissions import IsAuthor


class DeckViewSet(ViewSet):
    queryset = models.Deck.objects.select_related('difficulty', 'author').prefetch_related('tags').all()
    pagination_class = paginator.CustomPaginator

    def list(self, request):
        serializer = serializers.DeckSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)

class DeckOvnerViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = models.Deck.objects.all()

    def list(self, request):
        deck = self.queryset.filter(author=request.user)
        serializer = serializers.DeckSerializer(deck, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # queryset = self.queryset.filter(author=request.user, pk=pk)
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, deck)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)

