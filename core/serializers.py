import json
from dataclasses import dataclass

from rest_framework import serializers


class ImagemPostSerializer(serializers.Serializer):
    imagem = serializers.FileField()
    metricasProcessamentoImagem = serializers.JSONField(required=False)
    aplicarMetricasPosProcessamento = serializers.BooleanField(required=False)
    aplicarEscalaCinza = serializers.BooleanField(required=False)

class FiltroSerializer(serializers.Serializer):
    sigla = serializers.CharField()
    nome = serializers.CharField()
    descricao = serializers.CharField()
    exemplo = serializers.JSONField()


class ImagemRetornoPostSerializer(serializers.Serializer):
    erro = serializers.BooleanField()
    mensagemRetorno = serializers.CharField()
    identificacao = serializers.JSONField(required=False)
class ImagemRetorno:
    def __init__(self, erro, mensagemRetorno,identificacao=None):
        self.erro = erro
        self.mensagemRetorno = mensagemRetorno
        self.identificacao = identificacao

@dataclass
class ImagemResultadoDTOclass:
    classe: str
    precisao: str
    palavras_encontradas: json

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          ensure_ascii=False)