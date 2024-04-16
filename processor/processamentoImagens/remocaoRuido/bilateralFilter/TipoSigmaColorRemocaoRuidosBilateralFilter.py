from enum import Enum, unique
@unique
class TipoSigmaColorRemocaoRuidosBilateralFilter(Enum):

    metrica = 'sigmaColor'

    VALOR_INICIAL = 45
    VALOR_INTERMEDIARIO = 55
    VALOR_FINAL = 65
