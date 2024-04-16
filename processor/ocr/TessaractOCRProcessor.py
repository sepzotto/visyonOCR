import pytesseract
from pytesseract import Output
import main.settings as settings

def getResultadoOCR(img):
    resultado = pytesseract.image_to_data(img, lang=settings.TESSERACT_LANGUAGE, output_type=Output.DICT)
    return resultado['text']