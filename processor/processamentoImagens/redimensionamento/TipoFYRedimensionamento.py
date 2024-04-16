from enum import Enum, unique
@unique
class TipoFYRedimensionamento(Enum):
    metrica = 'fy'

    FY_05 = 0.5
    FY_15 = 1.5
    FY_2 = 2