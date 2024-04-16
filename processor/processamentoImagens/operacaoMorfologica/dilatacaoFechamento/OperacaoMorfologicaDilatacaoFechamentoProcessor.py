import cv2
import numpy as np

from processor.processamentoImagens.operacaoMorfologica.TipoIteracoesMatrizOperacaoMorfologica import \
    TipoIteracoesMatrizOperacaoMorfologica
from processor.processamentoImagens.operacaoMorfologica.TipoTamanhoMatrizOperacaoMorfologica import \
    TipoTamanhoMatrizOperacaoMorfologica


class OperacaoMorfologicaDilatacaoFechamentoProcessor:
    def efetuarConversao(img,sMatrix = None,iterations = None ):
        if sMatrix is None:
            sMatrix = TipoTamanhoMatrizOperacaoMorfologica.VALOR_INTERMEDIARIO.value
        if iterations is None:
            iterations = TipoIteracoesMatrizOperacaoMorfologica.VALOR_INTERMEDIARIO.value
        kernel = np.ones((sMatrix, sMatrix), np.uint8)
        dilatacao = cv2.dilate(img, kernel,iterations)
        # FECHAMENTO - APÓS A DILATACAO
        img_ret = cv2.erode(dilatacao, kernel,iterations)
        return img_ret,sMatrix,iterations