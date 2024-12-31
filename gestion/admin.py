from django.contrib import admin
from .models import User, Tache, Stock, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import TacheForm

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'statut', 'priorite', 'date_limite', 'utilisateur_assigne')
    autocomplete_fields = ['utilisateur_assigne']
    search_fields = ['titre', 'description']
    list_filter = ['statut', 'priorite', 'date_limite']

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    list_display = ['username', 'email', 'is_staff', 'is_active']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['article', 'quantite', 'seuil_critique', 'fournisseur']
    search_fields = ['article', 'fournisseur']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user__username', 'role']
