from rest_framework import serializers
from apps.mapas_paises.models import Paises, Capital


class CapitalSerializer(serializers.ModelSerializer):
    pais = serializers.StringRelatedField()
    
    class Meta:
        model = Capital
        fields = [
            'nome',
            'pais'
        ]
        
        
class PaisesSerializers(serializers.ModelSerializer):
    capital = CapitalSerializer()
    
    class Meta:
        model = Paises
        fields = [
            'nome',
            'populacao',
            'regiao',
            'subregiao',
            'capital'
        ]
