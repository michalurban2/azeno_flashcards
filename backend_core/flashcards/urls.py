from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets

app_name = 'flashcards'

router= DefaultRouter()
router.register(r'deck/', viewsets.DeckViewSet.as_view({'get':'list'}), basename='deck')
router.register(r'users/deck/', viewsets.DeckViewSet.as_view({'get':'list'}), basename='deck')


urlpatterns = [
    # path('flashcards/', views.FashCardsView.as_view(), name='flashcards'),
    path('flashcards/<int:rating>', views.FashCardsView.as_view(), name='flashcards'),
    path('flashcards/<int:pk>', views.FlashCardItemAsView.as_view(), name='flashcards'),
    *router.urls,
]

# urlpatterns += router.urls