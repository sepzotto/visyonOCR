from enum import Enum, unique
@unique
class TipoPreProcessamentoImagem(Enum):
    ROTACAO = 'ROT'
    LIMIARIZACAO = 'LOT'
    INVERSAO_CORES = 'INC'
    REMOCAO_RUIDOS = 'RFB'
    REDIMENSIONAMENTO = 'RED'
    OPERACAO_MORFOLOGICA_DI_FE = 'ODF'

