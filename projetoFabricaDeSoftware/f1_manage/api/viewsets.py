from rest_framework import viewsets
from f1_manage.api import serializers
from f1_manage import models

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = models.Piloto.objects.all()
    serializer_class = serializers.PilotoSerializer

    def get_queryset(self):
        queryset = models.Piloto.objects.all()

        equipe = self.request.query_params.get("equipe")
        nome = self.request.query_params.get("nome")

        if equipe:
            queryset = queryset.filter(equipe_id=equipe)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = models.Equipe.objects.all()
    serializer_class = serializers.EquipeSerializer