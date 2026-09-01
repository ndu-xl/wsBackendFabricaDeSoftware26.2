from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['OpenF1']
)
@api_view(['GET'])
def pilotos_openf1(request):
    try:
        numero = request.GET.get('numero')
        url = "https://api.openf1.org/v1/drivers?session_key=latest"
        if numero:
            url += f"&driver_number={numero}"
        resposta = requests.get(url, timeout=10)
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
    except requests.exceptions.Timeout:
        return Response({"erro":"A openF1 demorou muito para responder"}, status=status.HTTP_504_GATEWAY_TIMEOUT)
    except requests.exceptions.ConnectionError:
        return Response({"erro":"Não foi possivel conectar à openF1"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except requests.exceptions.RequestException:
        return Response({"erro":"Não foi possível acessar a API Open F1"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Create your views here.
