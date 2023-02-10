# Azeno Flashcards

## Algorytm postępowania

1. Czy potrzebujemy django app?
   1. `python manage.py startapp <name>`
   2. Dodaj do INSTALL APPS -> settings.py
2. Analiza czy potrzebujemy dane?
   1. Narysuj ERD diagram na kartce 
   2. Implementacja w models.py
   3. `python manage.py makemigrations <app_name>`
   4. `python manage.py migrate <app_name>`
   5. Unit test -> pytest
3. Czy potrzebujemy zarządzać tym zasobem z CMS (django admin)
   1. Rejestrujemy modele w admin.py
4. Czy wystawiamy dane widoku?
   1. tworzymy plik serializers.py (format danych) 
   2. Unit tests
5. Tworzymy widoki (logikę)
   1. Dobieramy odpowiednią klase do obsługi widoku [wyszukiwarka widoków](https://www.cdrf.co/)
   2. Widok musi zwracać response lub redirect
   3. Logika uprawnień permission.py
   4. Unit tests
6. Tworzymy lokalny ruter
   1. W pliku urls.py tworzymy urlpatterns lub router
   2. Podpinamy lokalne urls do globalnych -> config/urls.py
7. Postman i stworzenie kolekcji
   1. Wyeksportowanie kolekcji do repozytorium
