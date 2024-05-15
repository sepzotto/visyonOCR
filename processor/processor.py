import traceback

from core.serializers import ImagemRetorno
from processor.processamentoImagens.PreProcessamentoAgrupadoThreadProcessor import \
    PreProcessamentoAgrupadoThreadProcessor


def processarImagem(imagem,dados):
        try:
                if "imageProcessingMetrics" in dados:
                    metricasProcessamentoImagem = dados["imageProcessingMetrics"]
                else:
                    metricasProcessamentoImagem = None

                if "applyPostProcessingMetrics" in dados:
                    aplicarMetricasPosProcessamento = dados["applyPostProcessingMetrics"]
                else:
                    aplicarMetricasPosProcessamento = False

                if "applyGrayScale" in dados:
                    aplicarEscalaCinza = dados["applyGrayScale"]
                else:
                    aplicarEscalaCinza = False
                return realizarProcessamento(imagem,metricasProcessamentoImagem,aplicarMetricasPosProcessamento,aplicarEscalaCinza)
        except Exception as error:
                print('Error found: ', error)
                traceback.print_exc()
                return ImagemRetorno(True,error)
def realizarProcessamento(imagem,metricasProcessamentoImagem,aplicarMetricasPosProcessamento,aplicarEscalaCinza):
    identificacao = PreProcessamentoAgrupadoThreadProcessor.iniciarProcessamento(imagem, metricasProcessamentoImagem, aplicarMetricasPosProcessamento,aplicarEscalaCinza)
    if (identificacao is not None and len(identificacao) > 0):
        return ImagemRetorno(False, 'Image with identification pattern found',identificacao)
    else:
        return ImagemRetorno(False, 'Image without identification pattern')
