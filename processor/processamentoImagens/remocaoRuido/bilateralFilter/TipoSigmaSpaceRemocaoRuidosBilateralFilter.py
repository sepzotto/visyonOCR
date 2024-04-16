from enum import Enum, unique
@unique
class TipoSigmaSpaceRemocaoRuidosBilateralFilter(Enum):
    metrica = 'sigmaSpace'

    VALOR_INICIAL = 45
    VALOR_INTERMEDIARIO = 55
    VALOR_FINAL = 65
