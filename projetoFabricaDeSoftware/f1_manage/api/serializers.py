from rest_framework import serializers
from f1_manage import models

class PilotoSerializer(serializers.ModelSerializer):
    equipe_nome = serializers.CharField(
        source="equipe.nome",
        read_only=True
    )
    class Meta:
        model = models.Piloto
        fields = ['id','nome','numero','equipe','equipe_nome']


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipe
        fields = '__all__'