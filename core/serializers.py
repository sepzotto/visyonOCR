import json
from dataclasses import dataclass

from rest_framework import serializers


class ImagemPostSerializer(serializers.Serializer):
    image = serializers.FileField()
    imageProcessingMetrics = serializers.JSONField(required=False)
    applyPostProcessingMetrics = serializers.BooleanField(required=False)
    applyGrayScale = serializers.BooleanField(required=False)

class FiltroSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    example = serializers.JSONField()

class ImagemRetornoPostSerializer(serializers.Serializer):
    error = serializers.BooleanField()
    messageResponse = serializers.CharField()
    identification = serializers.JSONField(required=False)
class ImagemRetorno:
    def __init__(self, error, messageResponse,identification=None):
        self.error = error
        self.messageResponse = messageResponse
        self.identification = identification

@dataclass
class ImagemResultadoDTOclass:
    classe: str
    prediction: str
    found_words: json

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          ensure_ascii=False)