import traceback

from core.serializers import ImagemRetorno
from processor.processamentoImagens.PreProcessamentoAgrupadoThreadProcessor import \
    PreProcessamentoAgrupadoThreadProcessor


def processarImagem(imagem,dados):
        try:
                if "metricasProcessamentoImagem" in dados:
                    metricasProcessamentoImagem = dados["metricasProcessamentoImagem"]
                else:
                    metricasProcessamentoImagem = None

                if "aplicarMetricasPosProcessamento" in dados:
                    aplicarMetricasPosProcessamento = dados["aplicarMetricasPosProcessamento"]
                else:
                    aplicarMetricasPosProcessamento = False

                if "aplicarEscalaCinza" in dados:
                    aplicarEscalaCinza = dados["aplicarEscalaCinza"]
                else:
                    aplicarEscalaCinza = False
                return realizarProcessamento(imagem,metricasProcessamentoImagem,aplicarMetricasPosProcessamento,aplicarEscalaCinza)
        except Exception as error:
                print('Erro encontrado', error)
                traceback.print_exc()
                return ImagemRetorno(True,error)
def realizarProcessamento(imagem,metricasProcessamentoImagem,aplicarMetricasPosProcessamento,aplicarEscalaCinza):
    identificacao = PreProcessamentoAgrupadoThreadProcessor.iniciarProcessamento(imagem, metricasProcessamentoImagem, aplicarMetricasPosProcessamento,aplicarEscalaCinza)
    if (identificacao is not None and len(identificacao) > 0):
        return ImagemRetorno(False, 'Imagem com padrão de indentificação encontrada',identificacao)
    else:
        return ImagemRetorno(False, 'Imagem sem padrão de indentificação')
