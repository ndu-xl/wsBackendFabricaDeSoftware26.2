from rest_framework import serializers
from f1_manage import models

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Piloto
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipe
        fields = '__all__'