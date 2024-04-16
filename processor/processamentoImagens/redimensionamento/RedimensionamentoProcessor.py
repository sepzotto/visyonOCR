import cv2

from processor.processamentoImagens.redimensionamento.TipoFXRedimensionamento import TipoFXRedimensionamento
from processor.processamentoImagens.redimensionamento.TipoFYRedimensionamento import TipoFYRedimensionamento
from processor.processamentoImagens.redimensionamento.TipoInterpolationRedimensionamento import \
    TipoInterpolationRedimensionamento


class RedimensionamentoProcessor:
    def efetuarConversao(img,fx = None,fy = None,interpolation = None):
        if fx is None:
            fx = TipoFXRedimensionamento.FX_05.value
        if fy is None:
            fy = TipoFYRedimensionamento.FY_05.value
        if interpolation is None:
            interpolation = TipoInterpolationRedimensionamento.INTER_AREA.value
        img_ret = cv2.resize(img,None,fx=fx,fy=fy,interpolation=interpolation)
        return img_ret,fx,fy,interpolation
