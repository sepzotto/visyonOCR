import cv2

from processor.processamentoImagens.remocaoRuido.bilateralFilter.TipoDiameterRemocaoRuidosBilateralFilter import \
    TipoDiameterRemocaoRuidosBilateralFilter
from processor.processamentoImagens.remocaoRuido.bilateralFilter.TipoSigmaColorRemocaoRuidosBilateralFilter import \
    TipoSigmaColorRemocaoRuidosBilateralFilter
from processor.processamentoImagens.remocaoRuido.bilateralFilter.TipoSigmaSpaceRemocaoRuidosBilateralFilter import \
    TipoSigmaSpaceRemocaoRuidosBilateralFilter


class RemocaoRuidoBilateralFilterProcessor:

    def efetuarConversao(img,parametro=None):
        if parametro is None:
            diameter = TipoDiameterRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
            sigmaColor = TipoSigmaColorRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
            sigmaSpace = TipoSigmaSpaceRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
        else:
            if 'diameter' in parametro.keys():
                diameter = parametro["diameter"]
            else:
                diameter = TipoDiameterRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
            if 'sigmaColor' in parametro.keys():
                sigmaColor = parametro["sigmaColor"]
            else:
                sigmaColor = TipoSigmaColorRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
            if 'sigmaSpace' in parametro.keys():
                sigmaSpace = parametro["sigmaSpace"]
            else:
                sigmaSpace = TipoSigmaSpaceRemocaoRuidosBilateralFilter.VALOR_INTERMEDIARIO.value
        img_ret = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
        return img_ret,diameter,sigmaColor,sigmaSpace
