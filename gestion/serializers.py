from rest_framework.serializers import ModelSerializer
from .models import Tache, Prospect, Stock


class TacheSerializer(ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class ProspectSerializer(ModelSerializer):
    class Meta:
        model = Prospect
        fields = '__all__'


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
