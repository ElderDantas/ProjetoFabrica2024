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
    
    def list(self, request, *args, **kwargs):
        queryset = Capital.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PaisesViewSet(ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializers
    
    def create(self, request, *args, **kwargs):
        nome = request.data.get("nome")
        
        requisicao = requests.get(
            f'https://restcountries.com/v3.1/name/{nome}/'
        )
        
        requisicao_dicionario = json.loads(requisicao.content)[0]
        
        pais = Paises.objects.create(
            nome=requisicao_dicionario["name"]["common"],
            populacao=requisicao_dicionario["population"],
            regiao=requisicao_dicionario["region"],
            subregiao=requisicao_dicionario["subregion"],
        )
        
        capital_nome = capital=requisicao_dicionario["capital"][0]
        capital, created = Capital.objects.get_or_create(
            nome=capital_nome,
            pais=pais
        )
        
        pais.capital = capital
        pais.save()
        
        serializer = self.get_serializer(pais)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    