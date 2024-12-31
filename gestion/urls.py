from django.urls import path
from . import views
from gestion import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('taches/', views.liste_taches, name='liste_taches'),
    path('stocks/', views.liste_stocks, name='liste_stocks'),
    path('technicien/', views.espace_technicien, name='espace_technicien'),
    path('commercial/', views.espace_commercial, name='espace_commercial'),
    path('administrateur/', views.espace_administrateur, name='espace_administrateur'),
    path('tache/update/<int:tache_id>/', views.update_tache, name='update_tache'),
    path('', views.accueil, name='accueil'),
]
