from enum import Enum, unique
@unique
class TipoTrashHoldValueLimiarizacaoOTSU(Enum):
    metrica = 'trashHold'

    VALOR_INICIAL = 120
    VALOR_INTERMEDIARIO = 127
    VALOR_FINAL = 140
