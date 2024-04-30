from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import FiltroSerializer


class FilterViewList(APIView):
    def get(self, request):
        dados = [{"sigla": "INC", "nome": "Inversão de Cores","descricao":"Realiza a inversão de cores transformando a imagem que está em escala de cinza em branco e preto.","exemplo":"{'1':{'tipoProcessamento':'INC','parametros':{}}}"},
                 {"sigla": "LOT", "nome": "Limiarização OTSU","descricao":"Utilizado para se buscar o limiar ideal para separação dos elementos na imagem. Possui como parâmetro(s): (1). trashHoldValue:  Limite com valores pre definidos sendo possível informar os valores 120, 127 e 140.","exemplo":"{'1':{'tipoProcessamento':'LOT','parametros':{'trashHold':'127'}}}"},
                 {"sigla": "RFB", "nome": "Remoção de ruídos - Filtro Bilateral","descricao": "Usado para suavizar as imagens e reduzir o ruído, preservando as bordas. Possui como parâmetro(s): (1). diameter: Variável que representa o diámetro dos pixels vizinhos sendo possível informar os valores 5, 15, 30. (2). sigmaColor: Variável que representa o filtro sigma no espaço de cores sendo possível informar os valores 45, 55, 65. (3). sigmaSpace: Variável que representa o filtro sigma no espaço de coordenadas sendo possível informar os valores 45, 55, 65.","exemplo": "{'1':{'tipoProcessamento':'RFB','parametros':{'diameter': '15','sigmaColor': '45','sigmaSpace': '65}}}"},
                 {"sigla": "ROT", "nome": "Rotação", "descricao": "Usado para realizar a rotação das imagens. Possui como parâmetro(s): (1). rotatedegrees: Variável que representa o grau de rotação que será aplicado na imagem, podendo ser um número entre 1 e 359.","exemplo": "{'1':{'tipoProcessamento':'ROT','parametros': {'rotatedegrees': '90' }}}"},
                 {"sigla": "RED", "nome": "Redimensionamento","descricao": "Realiza o redimensionamento da imagem para permitir uma melhor resolução para o OCR. Possui como parâmetro(s): (1). fx: Fator de sacla sobrte o eixo horizontal. (2). fy: Fator de sacla sobrte o eixo vertical.","exemplo": "{'1':{'tipoProcessamento':'RED','parametros': {'fx': '2','fy': '2'}}}"},
                 {"sigla": "ODF", "nome": "Operação Morfológica - Dilatação e Fechamento","descricao": "Irá ajustar os limites do objeto em primeiro plano e aumentar a área do objeto para acentuar recursos. Possui como parâmetro(s): (1). sMatrix: O kernel a ser usado. (2). iterations: O número de iterações de dilatações a serem realizadas.","exemplo": "{'1':{'tipoProcessamento':'ODF','parametros': {'sMatrix': '2','iterations': '3'}}}"}
                 ]
        results = FiltroSerializer(dados, many=True).data
        return Response(results)