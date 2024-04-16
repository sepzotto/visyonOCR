from enum import Enum, unique
@unique
class TipoFXRedimensionamento(Enum):
    metrica = 'fx'

    FX_05 = 0.5
    FX_15 = 1.5
    FX_2 = 2

