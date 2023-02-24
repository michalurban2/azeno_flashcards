from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import FlashCard, Deck, Tag, DifficultyLevel


class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('id', 'question', 'answer', 'author', 'category', 'difficulty', 'rating', 'tags', 'decks')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        modle= DifficultyLevel
        fields = ('name', 'value')


class DeckSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Deck
        fields = ('id', 'category', 'difficulty', 'rating', 'tags', 'name', 'description', 'is_public', 'author_email')
