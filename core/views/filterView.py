from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import FiltroSerializer


class FilterViewList(APIView):
    def get(self, request):
        dados = [{"id": "INC", "name": "Color Inversion","description":"Performs color inversion, transforming the grayscale image into black and white.","example":"{'1':{'processingType':'INC','parameters':{}}}"},
                 {"id": "LOT", "name": "OTSU Thresholding","description":"Used to find the ideal threshold for separating elements in the image. It has parameter(s): (1). trashHoldValue:  Threshold with predefined values, where it's possible to inform the values 120, 127, and 140.","example":"{'1':{'processingType':'LOT','parameters':{'trashHold':'127'}}}"},
                 {"id": "RFB", "name": "Noise Removal - Bilateral Filter","description": "Used to smooth images and reduce noise while preserving edges. It has parameter(s): (1) diameter: Variable representing the diameter of neighboring pixels, with possible values of 5, 15, 30. (2) sigmaColor: Variable representing the sigma filter in color space, with possible values of 45, 55, 65. (3) sigmaSpace: Variable representing the sigma filter in coordinate space, with possible values of 45, 55, 65.","example": "{'1':{'processingType':'RFB','parameters':{'diameter': '15','sigmaColor': '45','sigmaSpace': '65}}}"},
                 {"id": "ROT", "name": "Rotation", "description": "Used to perform image rotation. It has the following parameter: (1) rotatedegrees: Variable representing the degree of rotation to be applied to the image, which can be a number between 1 and 359.","example": "{'1':{'processingType':'ROT','parameters': {'rotatedegrees': '90' }}}"},
                 {"id": "RED", "name": "Resizing","description": "Resizes the image to allow for better resolution for OCR. It has the following parameters: (1) fx: Scale factor on the horizontal axis. (2) fy: Scale factor on the vertical axis.","example": "{'1':{'processingType':'RED','parameters': {'fx': '2','fy': '2'}}}"},
                 {"id": "ODF", "name": "Morphological Operation - Dilation and Closing","description": "It will adjust the boundaries of the foreground object and increase the area of the object to enhance features. It has the following parameters: (1) sMatrix: The kernel to be used. (2) iterations: The number of dilation iterations to be performed.","example": "{'1':{'processingType':'ODF','parameters': {'sMatrix': '2','iterations': '3'}}}"}
                 ]
        results = FiltroSerializer(dados, many=True).data
        return Response(results)