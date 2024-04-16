from enum import Enum, unique

import cv2


@unique
class TipoInterpolationRedimensionamento(Enum):
    INTER_NEAREST = cv2.INTER_NEAREST
    INTER_LINEAR = cv2.INTER_LINEAR
    INTER_AREA = cv2.INTER_AREA
    INTER_CUBIC = cv2.INTER_CUBIC
    INTER_LANCZOS4 = cv2.INTER_LANCZOS4

