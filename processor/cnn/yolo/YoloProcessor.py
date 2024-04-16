import os

import cv2
import numpy as np

import main.settings as settings


def carregarRede():
  weights_path = os.path.sep.join([settings.DATASET_YOLO_CNN_PATH, 'rede_neural.weights'])
  config_path = os.path.sep.join([settings.DATASET_YOLO_CFG_PATH, 'yolov4_custom.cfg'])
  return cv2.dnn.readNet(config_path, weights_path)

def getImagensYolo(imagem,net,precisaominima=None):
  #Carregando a rede
  if(precisaominima == None):
    threshold = settings.CNN_MIN_PREDICTION
  else:
    threshold = precisaominima
  labels_path = os.path.sep.join([settings.DATASET_YOLO_DATA_PATH, 'obj.names'])
  LABELS = open(labels_path).read().strip().split('\n')

  COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype='uint8')
  ln = net.getLayerNames()
  ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
  type(imagem)
  imagem_cp = imagem.copy()
  (H, W) = imagem.shape[:2]

  blob = cv2.dnn.blobFromImage(imagem, 1 / 255.0, (608, 608), swapRB = True, crop = False)
  net.setInput(blob)
  layer_outputs = net.forward(ln)
  threshold_NMS = 0.3
  caixas = []
  confiancas = []
  IDclasses = []
  for output in layer_outputs:
    for detection in output:
      scores = detection[5:]
      classeID = np.argmax(scores)
      confianca = scores[classeID]
      if confianca > threshold:
        caixa = detection[0:4] * np.array([W, H, W, H])
        (centerX, centerY, width, height) = caixa.astype('int')
        x = int(centerX - (width / 2))
        y = int(centerY - (height / 2))
        caixas.append([x, y, int(width), int(height)])
        confiancas.append(float(confianca))
        IDclasses.append(classeID)

  objs = cv2.dnn.NMSBoxes(caixas, confiancas, threshold, threshold_NMS)

  arrayImagensEncontradas = []
  if len(objs) > 0:
    for i in objs.flatten():
      (x, y) = (corrigeSize(caixas[i][0]-5), corrigeSize(caixas[i][1]))
      (w, h) = (corrigeSize(caixas[i][2]+5), corrigeSize(caixas[i][3]))
      objeto = imagem_cp[y:y + h, x:x + w]
      arrayImagensEncontradas.append([objeto,LABELS[IDclasses[i]],confiancas[i]])
      cor = [int(c) for c in COLORS[IDclasses[i]]]
      cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
      texto = "{}: {:.4f}".format(LABELS[IDclasses[i]], confiancas[i])
      cv2.putText(imagem, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)
  return arrayImagensEncontradas


def corrigeSize(z):
  if (z > 0):
    z = z
  else:
    z = 1
  return z
