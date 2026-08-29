from rest_framework import viewsets
from f1_manage.api import serializers
from f1_manage import models

class PilotoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PilotoSerializer
    queryset = models.Piloto.objects.all()