from django.contrib import admin
from django.urls import path, include
from gestion.views import espace_technicien, espace_commercial, espace_administrateur
from gestion import views


urlpatterns = [
    path('admin/', admin.site.urls),  # Interface admin
    path('api/', include('gestion.urls')),  # Inclusion des routes API
    path('', espace_administrateur, name='dashboard'),  # Page d'accueil
    path('technicien/', espace_technicien, name='technicien'),  # Vue technicien
    path('commercial/', espace_commercial, name='commercial'),  # Vue commercial
    path('administrateur/', espace_administrateur, name='administrateur'),  # Vue administrateur
    path('', include('gestion.urls')),  # Inclure les routes de l'application gestion
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
