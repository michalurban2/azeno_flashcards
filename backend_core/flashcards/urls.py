from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    # path('flashcards/', views.FashCardsView.as_view(), name='flashcards'),
    path('flashcards/<int:rating>', views.FashCardsView.as_view(), name='flashcards'),
    path('flashcards/<int:pk>', views.FlashCardItemAsView.as_view(), name='flashcards'),

]