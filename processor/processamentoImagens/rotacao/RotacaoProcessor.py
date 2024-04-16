import numpy as np
from PIL import Image
class RotacaoProcessor:

    def efetuarConversao(imagem,aplicarEscalaCinza,parametros = None):
        if(parametros is None):
            rotatedegrees = 0
        else:
            rotatedegrees = parametros["rotatedegrees"]
        if (aplicarEscalaCinza):
            img = Image.fromarray(imagem, 'L')
        else:
            img = Image.fromarray(imagem, 'RGB')
        if rotatedegrees != None and rotatedegrees > 0:
            img = img.rotate(rotatedegrees)
        return np.array(img),rotatedegrees
