from django.contrib import admin
from django.urls import path, include
from gestion.views import espace_technicien, espace_commercial, espace_administrateur, dashboard, liste_taches, liste_stocks
from . import views
from gestion import views


urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'administration Django
    path('api/', include('gestion.urls')),  # Inclure les URLs de l'application gestion
    path('', dashboard, name='dashboard'),  # Vue principale
    path('technicien/', espace_technicien, name='technicien'),  # Vue pour les techniciens
    path('commercial/', espace_commercial, name='commercial'),  # Vue pour les commerciaux
    path('administrateur/', espace_administrateur, name='administrateur'),  # Vue pour les administrateurs
    path('taches/', liste_taches, name='liste_taches'),  # Liste des tâches
    path('stocks/', liste_stocks, name='liste_stocks'),  # Liste des stocks
    path('', include('gestion.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('taches/', views.liste_taches, name='liste_taches'),
    path('stocks/', views.liste_stocks, name='liste_stocks'),
    path('technicien/', views.espace_technicien, name='espace_technicien'),
    path('commercial/', views.espace_commercial, name='espace_commercial'),
    path('administrateur/', views.espace_administrateur, name='espace_administrateur'),
    path('tache/update/<int:tache_id>/', views.update_tache, name='update_tache'),
    path('', views.accueil, name='accueil'),
    path('technicien/', views.espace_technicien, name='technicien'),
    path('commercial/', views.espace_commercial, name='commercial'),
    path('administrateur/', views.espace_administrateur, name='administrateur'),
]
