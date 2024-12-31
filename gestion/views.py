from rest_framework.viewsets import ModelViewSet
from .models import Tache, Prospect, Stock
from .serializers import TacheSerializer, ProspectSerializer, StockSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# API Views
class TacheViewSet(ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class ProspectViewSet(ModelViewSet):
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# Dashboard
@login_required
def dashboard(request):
    taches_count = Tache.objects.count()
    stocks_count = Stock.objects.count()
    prospects_count = Prospect.objects.count()
    return render(request, 'dashboard.html', {
        'taches_count': taches_count,
        'stocks_count': stocks_count,
        'prospects_count': prospects_count,
    })

# Liste des tâches
@login_required
def liste_taches(request):
    from .models import Tache
    taches = Tache.objects.filter(utilisateur_assigne=request.user)  # Filtre par utilisateur connecté
    return render(request, 'liste_taches.html', {'taches': taches})

# Liste des stocks
@login_required
def liste_stocks(request):
    from .models import Stock
    stocks = Stock.objects.all()  # Récupère tous les stocks
    return render(request, 'liste_stocks.html', {'stocks': stocks})

# Espace pour les commerciaux
@login_required
def espace_commercial(request):
    prospects = Prospect.objects.all()
    return render(request, 'gestion/commercial.html', {'prospects': prospects})

# Espace pour les techniciens
@login_required
def espace_technicien(request):
    from .models import Tache
    utilisateur = request.user
    taches = Tache.objects.filter(utilisateur_assigne=utilisateur)  # Filtre par utilisateur assigné
    return render(request, 'gestion/technicien.html', {'taches': taches})



# Mise à jour d'une tâche
@login_required
def update_tache(request, tache_id):
    if request.method == "POST":
        try:
            tache = Tache.objects.get(id=tache_id, utilisateur_assigne=request.user)
            tache.statut = request.POST.get('statut')
            tache.save()
        except Tache.DoesNotExist:
            pass
    return redirect('espace_technicien')

# Espace administrateur
@login_required
def espace_administrateur(request):
    stocks = Stock.objects.all()
    taches = Tache.objects.all()
    return render(request, 'gestion/administrateur.html', {'stocks': stocks, 'taches': taches})

# Accueil
def accueil(request):
    return render(request, 'gestion/accueil.html')








# Dashboard
def dashboard(request):
    taches_count = Tache.objects.count()
    stocks_count = Stock.objects.aggregate(total_stock=models.Sum('quantite'))['total_stock'] or 0
    prospects_count = 10  # Exemple de données statiques
    return render(request, 'dashboard.html', {
        'taches_count': taches_count,
        'stocks_count': stocks_count,
        'prospects_count': prospects_count,
    })

# Liste des tâches
def liste_taches(request):
    taches = Tache.objects.all()
    return render(request, 'liste_taches.html', {'taches': taches})

# Espace Technicien
def espace_technicien(request):
    utilisateur = request.user
    taches = Tache.objects.filter(utilisateur_assigne=utilisateur)
    return render(request, 'espace_technicien.html', {'taches': taches})

# Espace Commercial
def espace_commercial(request):
    return render(request, 'espace_commercial.html')

# Espace Administrateur
def espace_administrateur(request):
    return render(request, 'espace_administrateur.html')
