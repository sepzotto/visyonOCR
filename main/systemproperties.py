#versao3-local.py - para computador local
#Imprime versao de Tensorflow, Keras e Keras dentro do Tensorflow
#Tambem imprime se GPU esta funcionando, versao de SO, CPU e RAM
import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
# Coloque o comando abaixo, quando da erro "Failed to get convolution algorithm"
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
import keras
import sys; import cv2
import tensorflow as tf


print("Versao python3:",sys.version)
print("Versao de tensorflow:",tf.__version__)
print("Versao de Keras independente:",keras.__version__)
print("Versao de Keras dentro de tensorflow:",tf.keras.__version__)
print("Versao cv2:",cv2.__version__)
os.system("nvcc --version | grep release")
print()
gpu=tf.test.gpu_device_name()
if gpu=="":
 print("Computador sem GPU.")
else:
 print("Computador com GPU:",tf.test.gpu_device_name())
 from tensorflow.python.client import device_lib
 devices=device_lib.list_local_devices()
 print("Dispositivos:",[x.physical_device_desc for x in devices if x.physical_device_desc!=""])
 os.system('cat /usr/include/cudnn.h | grep "define CUDNN_MAJOR" -A 2')
 #os.system('nvidia-smi')
print()
os.system('lsb_release -a | grep "Description"') #imprime qual é o sistema operacional
os.system('cat /proc/cpuinfo | grep -E "model name"') #especificações de CPU
os.system('cat /proc/meminfo | grep "Mem"') #especificações de RAM
print()
#import torch;
#print("Versao pytorch: ",torch.__version__);
#print("GPU disponivel em pytorch: ",torch.cuda.is_available());
#os.system('df -H')