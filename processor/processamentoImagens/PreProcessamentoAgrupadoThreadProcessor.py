import json

import cv2
import numpy as np
import processor.cnn.yolo.YoloProcessor as YoloCNN
import processor.ocr.TessaractOCRProcessor as ocr
import processor.util.Utilidades as util
from core.serializers import ImagemResultadoDTOclass
import main.settings as st

class PreProcessamentoAgrupadoThreadProcessor:

    def iniciarProcessamento(imagemOriginal,parametros,aplicarMetricasPosProcessamento,aplicarEscalaCinza):
        resultados = []

        if(st.EXIBIR_IMAGENS_MD):
            util.mostraPil(imagemOriginal)

        #Conversao para escala de cinza
        if(aplicarEscalaCinza is True):
            imgProcessada = util.converteImagemEscalaCinza(np.array(imagemOriginal))
            if (st.EXIBIR_IMAGENS_MD):
                util.mostrar(imgProcessada)
        else:
            imgProcessada = np.array(imagemOriginal)

        # Aplicação de filtros - pre processamento
        if (parametros is not None and len(parametros) > 0 and aplicarMetricasPosProcessamento is False):
           imgProcessada = PreProcessamentoAgrupadoThreadProcessor.getResultadoProcessamentoImagens(imgProcessada, parametros,aplicarEscalaCinza)
           if (st.EXIBIR_IMAGENS_MD):
               util.mostraPil(imgProcessada)

        # Aplica a rede neural Yolo e obtem os boundi box específicos
        imagesYoloResult  = YoloCNN.getImagensYolo(cv2.cvtColor(imgProcessada, cv2.COLOR_RGB2BGR),YoloCNN.carregarRede())

        for imageYolo in imagesYoloResult:
           classe = imageYolo[1]
           previsao = "{:.2%}".format(imageYolo[2])
           if (aplicarEscalaCinza is True):
               imgY = util.converteImagemEscalaCinza(imageYolo[0])
           else:
                imgY = imageYolo[0]

           # Aplicação de filtros - pós processamento
           if (parametros is not None and len(parametros) > 0 and aplicarMetricasPosProcessamento is True):
               imgY = PreProcessamentoAgrupadoThreadProcessor.getResultadoProcessamentoImagens(imgY, parametros,aplicarEscalaCinza)

           if (st.EXIBIR_IMAGENS_MD):
               util.mostrar(imgY)

           ocr = PreProcessamentoAgrupadoThreadProcessor.getResultadoOCR(imgY)
           resProcessamento = ImagemResultadoDTOclass(**{'classe': classe, 'previsao': previsao, 'palavras_encontradas': [x for x in ocr if x.strip() != '']})
           resultados.append(resProcessamento.toJSON())
        return resultados

    def getResultadoProcessamentoImagens(imgProcessada, parametros,aplicarEscalaCinza):
        json_object = json.loads(parametros)
        json_object = dict(sorted(json_object.items()))
        for i in json_object:
            processamento = json_object[i]
            imgProcessada = util.getProcessamentoDic(processamento["tipoProcessamento"], imgProcessada,aplicarEscalaCinza,processamento["parametros"])
        return imgProcessada

    def getResultadoOCR(imgFile):
        return ocr.getResultadoOCR(imgFile)