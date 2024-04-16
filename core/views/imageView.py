from PIL import Image
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

import processor.processor as proc
from core.serializers import ImagemPostSerializer, ImagemRetornoPostSerializer


class ImagePostGeneric(CreateAPIView):
        def post(self, request):
            img = Image.open(request.FILES["imagem"])
            serializer_class = ImagemPostSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            retorno = proc.processarImagem(img,serializer_class.data)
            retornoSerializer = ImagemRetornoPostSerializer(retorno)
            return Response(retornoSerializer.data)


