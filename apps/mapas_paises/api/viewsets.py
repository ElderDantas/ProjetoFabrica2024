from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from apps.mapas_paises.models import Paises, Capital
from apps.mapas_paises.api.serializers import PaisesSerializers, CapitalSerializer
import requests
import json


class CapitalViewSet(ModelViewSet):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    
    def create(self, request, *args, **kwargs):
        nome_capital = request.data.get("nome")
        
        requisicao_capital = requests.get(
            f'https://restcountries.com/v3.1/capital/{nome_capital}/'
        )
        
        dicionario_capital = json.loads(requisicao_capital.content)[0]
        
    # def list(self, request, *args, **kwargs):
    #     queryset = Capital.objects.all()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class PaisesViewSet(ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializers
    
    def create(self, request, *args, **kwargs):
        nome = request.data.get("nome")
        
        requisicao = requests.get(
            f'https://restcountries.com/v3.1/name/{nome}/'
        )
        
        pais_dicionario = json.loads(requisicao.content)[0]
        
        pais = Paises.objects.create(
            nome=pais_dicionario["name"]["common"],
            populacao=pais_dicionario["population"],
            regiao=pais_dicionario["region"],
            subregiao=pais_dicionario["subregion"],
        )
        
        capital = pais_dicionario["capital"][0]
        capital, created = Capital.objects.get_or_create(
            nome=capital,
            pais=pais
        )
        
        pais.capital = capital
        pais.save()
        
        serializer = self.get_serializer(pais)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    