from rest_framework import viewsets
from f1_manage.api import serializers
from f1_manage import models

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = models.Piloto.objects.all()
    serializer_class = serializers.PilotoSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = models.Equipe.objects.all()
    serializer_class = serializers.EquipeSerializer