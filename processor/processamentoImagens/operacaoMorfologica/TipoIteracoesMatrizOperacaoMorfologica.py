from enum import Enum, unique
@unique
class TipoIteracoesMatrizOperacaoMorfologica(Enum):
    metrica = 'iterations'

    VALOR_INICIAL = 1
    VALOR_INTERMEDIARIO = 2
    VALOR_FINAL = 3
