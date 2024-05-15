import os

import main.settings as settings

#CÓDIGO QUE GERA O ARQUIVO TEST.TXT PARA O TREINAMENTO DA REDE
imagens = []
for filename in os.listdir(settings.DATASET_YOLO_VALID_PATH):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".JPEG") or filename.endswith(".png") or filename.endswith(".PNG") :
        imagens.append("data" + settings.SEPARATOR + "valid" + settings.SEPARATOR + filename)

with open(settings.DATASET_YOLO_DATA_PATH + settings.SEPARATOR + 'test.txt', "w") as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write("\n")
    outfile.close()

#CÓDIGO QUE GERA O ARQUIVO TRAIN.TXT PARA O TREINAMENTO DA REDE
imagens = []
for filename in os.listdir(settings.DATASET_YOLO_OBJ_PATH):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".JPEG") or filename.endswith(".png") or filename.endswith(".PNG") :
        imagens.append("data" + settings.SEPARATOR + "obj" + settings.SEPARATOR + filename)

with open(settings.DATASET_YOLO_DATA_PATH + settings.SEPARATOR + 'train.txt', 'w') as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write("\n")
    outfile.close()