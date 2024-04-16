import cv2

from processor.processamentoImagens.limiarizacao.limiarizacaoOTSU.TipoTrashHoldValueLimiarizacaoOTSU import \
    TipoTrashHoldValueLimiarizacaoOTSU


class LimiarizacaoOTSUProcessor:

    def efetuarConversao(img,parametros = None):
        if(parametros is None):
            thresholdValue = TipoTrashHoldValueLimiarizacaoOTSU.VALOR_INTERMEDIARIO.value
        else:
            thresholdValue = parametros["thresholdValue"]
        val, img_ret = cv2.threshold(img,thresholdValue,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return img_ret,thresholdValue
