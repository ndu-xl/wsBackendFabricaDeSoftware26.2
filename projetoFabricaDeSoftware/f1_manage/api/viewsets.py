from rest_framework import viewsets
from f1_manage.api import serializers
from f1_manage import models
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample

@extend_schema_view(
    list=extend_schema(
        summary='Listar pilotos',
        description='Retorna todos os pilotos cadastrados.'
    ),
    retrieve=extend_schema(
        summary='Consultar piloto',
        description='Retorna os dados de um piloto específico através do ID.'
    ),
    create=extend_schema(
    summary='Cadastrar piloto',
    description='Cadastra um novo piloto no banco de dados.',
    examples=[
        OpenApiExample(
            'Exemplo de piloto',
            value={
                'nome': 'Lewis Hamilton',
                'numero': 44,
                'equipe': 'Ferrari'
            },
            request_only=True
        )
    ]
    ),
    update=extend_schema(
        summary='Atualizar piloto',
        description='Atualiza completamente os dados de um piloto.'
    ),
    partial_update=extend_schema(
        summary='Atualizar parcialmente piloto',
        description='Atualiza parcialmente os dados de um piloto.'
    ),
    destroy=extend_schema(
        summary='Excluir piloto',
        description='Remove um piloto do banco de dados.'
    ),
)
@extend_schema(tags=['Pilotos'])
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

@extend_schema_view(
    list=extend_schema(
        summary='Listar equipes',
        description='Retorna todas as equipes cadastradas.'
    ),
    retrieve=extend_schema(
        summary='Consultar equipe',
        description='Retorna os dados de uma equipe específica através do ID.'
    ),
    create=extend_schema(
        summary='Cadastrar equipe',
        description='Cadastra uma nova equipe no banco de dados.',
        examples=[
            OpenApiExample(
                'Exemplo de equipe',
                value={
                    'nome': 'Ferrari',
                    'pais': 'Itália'
                },
                request_only=True
            )
        ]  
    ),
    update=extend_schema(
        summary='Atualizar equipe',
        description='Atualiza completamente os dados de uma equipe.'
    ),
    partial_update=extend_schema(
        summary='Atualizar parcialmente equipe',
        description='Atualiza parcialmente os dados de uma equipe.'
    ),
    destroy=extend_schema(
        summary='Excluir equipe',
        description='Remove uma equipe do banco de dados.'
    ),
)
@extend_schema(tags=['Equipes'])
class EquipeViewSet(viewsets.ModelViewSet):
    queryset = models.Equipe.objects.all()
    serializer_class = serializers.EquipeSerializer
