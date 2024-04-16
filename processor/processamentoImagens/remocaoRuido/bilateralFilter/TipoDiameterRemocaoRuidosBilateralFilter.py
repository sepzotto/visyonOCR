from enum import Enum, unique
@unique
class TipoDiameterRemocaoRuidosBilateralFilter(Enum):
    metrica = 'diameter'

    VALOR_INICIAL = 5
    VALOR_INTERMEDIARIO = 15
    VALOR_FINAL = 30
