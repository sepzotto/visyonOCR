import cv2
import matplotlib.pyplot as plt

from processor.processamentoImagens.TipoPreProcessamentoImagem import TipoPreProcessamentoImagem
from processor.processamentoImagens.inversaoCores.InversaoCoresProcessor import InversaoCoresProcessor
from processor.processamentoImagens.limiarizacao.limiarizacaoOTSU.LimiarizacaoOTSUProcessor import \
    LimiarizacaoOTSUProcessor
from processor.processamentoImagens.operacaoMorfologica.dilatacaoFechamento.OperacaoMorfologicaDilatacaoFechamentoProcessor import \
    OperacaoMorfologicaDilatacaoFechamentoProcessor
from processor.processamentoImagens.redimensionamento.RedimensionamentoProcessor import RedimensionamentoProcessor
from processor.processamentoImagens.remocaoRuido.bilateralFilter.RemocaoRuidoBilateralFilterProcessor import \
    RemocaoRuidoBilateralFilterProcessor
from processor.processamentoImagens.rotacao.RotacaoProcessor import RotacaoProcessor


def getProcessamentoDic(tipoPreProcessamentoImagem,img,aplicarEscalaCinza,parametros=None,):
    match(tipoPreProcessamentoImagem):
        case TipoPreProcessamentoImagem.LIMIARIZACAO.value:
            #Limiarizacao OTSU
            img_ret, thresholdValue = LimiarizacaoOTSUProcessor.efetuarConversao(img,parametros)
            return img_ret
        case TipoPreProcessamentoImagem.INVERSAO_CORES.value:
            img_ret = InversaoCoresProcessor.efetuarConversao(img)
            return img_ret
        case TipoPreProcessamentoImagem.REMOCAO_RUIDOS.value:
            #Remocao Ruidos Filtro Bilateral
            img_ret, diameter, sigmaColor, sigmaSpace = RemocaoRuidoBilateralFilterProcessor.efetuarConversao(img,parametros)
            return img_ret
        case TipoPreProcessamentoImagem.ROTACAO.value:
            #Rotação
            img_ret,rotatedegrees = RotacaoProcessor.efetuarConversao(img,aplicarEscalaCinza,parametros)
            return img_ret
        case TipoPreProcessamentoImagem.REDIMENSIONAMENTO.value:
            #Redimensionamento
            img_ret,fx,fy,interpolation = RedimensionamentoProcessor.efetuarConversao(img)
            return img_ret
        case TipoPreProcessamentoImagem.OPERACAO_MORFOLOGICA_DI_FE.value:
            # Operação Morfológica - dilatacao fechamento
            img_ret, sMatrix, iterations = OperacaoMorfologicaDilatacaoFechamentoProcessor.efetuarConversao(img)
            return img_ret
    return img

def mostrar(img):
        fig = plt.gcf()
        fig.set_size_inches(5, 5)
        plt.axis("off")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

def mostraPil(img):
    plt.imshow(img)
    plt.show()

def converteImagemEscalaCinza(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
