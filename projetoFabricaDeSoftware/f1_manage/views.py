from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def pilotos_openf1(request):
    try:
        resposta = requests.get("https://api.openf1.org/v1/drivers?session_key=latest")
        resposta.raise_for_status()
        dados = resposta.json()
        pilotos = []
        for piloto in dados:
            pilotos.append({
                "nome": piloto["full_name"],
                "numero": piloto["driver_number"],
                "equipe": piloto["team_name"]
            })
        return Response(pilotos)
    except requests.exceptions.RequestException:
        return Response({"erro":"Não foi possível acessar a API Open F1"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Create your views here.
