from django.test import TestCase
from gestion.models import Tache, Stock, Prospect

class TacheModelTest(TestCase):
    def test_create_tache(self):
        """Test de création d'une tâche."""
        tache = Tache.objects.create(
            titre="Test Task",
            description="Test Description",
            priorite="Moyenne",
            statut="A faire"
        )
        self.assertEqual(tache.titre, "Test Task")
        self.assertEqual(tache.priorite, "Moyenne")

class StockModelTest(TestCase):
    def test_create_stock(self):
        """Test de création d'un stock."""
        stock = Stock.objects.create(
            article="Test Item",
            quantite=10,
            seuil_critique=5,
            fournisseur="Test Supplier"
        )
        self.assertEqual(stock.article, "Test Item")
        self.assertEqual(stock.quantite, 10)

class ProspectModelTest(TestCase):
    def test_create_prospect(self):
        """Test de création d'un prospect."""
        prospect = Prospect.objects.create(
            nom="Test Prospect",
            entreprise="Test Company",
            telephone="123456789",
            email="test@test.com",
            dernier_contact="2024-12-31"
        )
        self.assertEqual(prospect.nom, "Test Prospect")
        self.assertEqual(prospect.email, "test@test.com")
