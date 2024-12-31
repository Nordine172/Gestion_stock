from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    roles = models.CharField(
        max_length=20,
        choices=[
            ('technicien', 'Technicien'),
            ('commercial', 'Commercial'),
            ('admin', 'Admin')
        ],
        default='admin'
    )

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'gestion'

class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[('A faire', 'À faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')],
        default='A faire'
    )
    priorite = models.CharField(
        max_length=20,
        choices=[('Basse', 'Basse'), ('Moyenne', 'Moyenne'), ('Haute', 'Haute')],
        default='Moyenne'
    )
    date_limite = models.DateField(blank=True, null=True)
    utilisateur_assigne = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='taches_assignes'
    )

    class Meta:
        app_label = 'gestion'

class Stock(models.Model):
    article = models.CharField(max_length=255)
    quantite = models.PositiveIntegerField()
    seuil_critique = models.PositiveIntegerField()
    fournisseur = models.CharField(max_length=255)

    def __str__(self):
        return self.article

    class Meta:
        app_label = 'gestion'


class Prospect(models.Model):
    nom = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    dernier_contact = models.DateField()
    statut = models.CharField(max_length=50, default='Actif')

    def __str__(self):
        return self.nom

    class Meta:
        app_label = 'gestion'

class Profile(models.Model):
    """Modèle pour les profils des utilisateurs"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=[
        ('technicien', 'Technicien'),
        ('commercial', 'Commercial'),
        ('admin', 'Admin'),
    ])

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        app_label = 'gestion'

