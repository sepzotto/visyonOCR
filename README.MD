# VisyonOCR

<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=Python&message=3.10&color=red&style=for-the-badge&logo=PYTHON"/>

O VisyonOCR é um sistema em python que combina técnicas de processamento de imagens, redes YOLO (You Only Look Once) e Reconhecimento Óptico de Caracteres (OCR) para oferecer uma solução completa de extração de texto em imagens.

---
### 1. Versão
#### 1.0
Disponibilização da aplicação com instruções de treinamento da rede neural e como usar o projeto para identificação textual podendo aplicar filtros de processamento de imagens.


---
### 2. Instalando o VisyonOCR pelo Git
```
git clone https://github.com/libgit2/libgit2
```

---
### 3. Ferramentas de Desenvolvimento Utilizadas
##### 3.1 PyCharm 2024.1 (Community Edition)

#### 3.2 Tesseract
```
Instalando e configurando o tesseract no Linux
--sudo add-apt-repository ppa:deadsnakes/ppa -y
--sudo add-apt-repository ppa:deadsnakes/nightly -y
--sudo apt update
--sudo apt install python3.10
--python3.10 --version
--sudo apt install python3.10-dev libpq-dev
```
```
Instalando e configurando o tesseract no Windows
https://github.com/UB-Mannheim/tesseract/wiki
```
```
Configurando o tesseract no projeto
--sudo apt install tesseract-ocr
--sudo apt install libtesseract-dev
--sudo apt-get install tesseract-ocr-por
```
```
Baixando a linguagem português
https://github.com/tesseract-ocr/tessdata/tree/3.04.00
Colocar em tessdata no local em que o tesseract foi instalado
```
#### 3.3 Principais Bibliotecas do Python
```
pip install --upgrade pip
pip install django
pip install opencv-python
pip install --upgrade Pillow
pip install numpy opencv-contrib-python
pip install pytesseract
pip install pyspellchecker
pip install unidecode
pip install matplotlib
pip install djangorestframework
pip install psycopg2
pip install django-rest-swagger
pip install drf-spectacular
pip install shapely
```

#### 3.4 Projeto para definição das áreas de interesse (Bounding Box)
https://github.com/HumanSignal/labelImg


#### 3.5 Google Colab - Treinamento da Rede Yolo
https://colab.research.google.com/drive/1Z2TfoZOjwlpqY-XLRoXvaQH2jWP57zlm?usp=sharing

#### 3.6 Ferramenta de Testes (API)

https://www.postman.com/

---

### 4. Configurando o Projeto
Abra o arquivo **main/settings.py** e realize a configuração dos principais pontos do sistema:
* PATH_URL: Nome do projeto quando for realizada a execução (Default: visyonOCR)
* WINDOWS: Se True indicará que o SO utilizado é Windows. Se False Linux (Default False)
* EXIBIR_IMAGENS_MD: Irá exibir as imagens no processo de identificação (Default False)
* CNN_MIN_PREDICTION: Previsão mínima para rede YOLO considerar a predição (Default= 0.70 )
* pytesseract.pytesseract.tesseract_cmd: Local onde o Tesseract está instalado (Default= r"/usr/bin/tesseract")
* TESSERACT_LANGUAGE: Idioma do Tesseract (Default= "eng", para portugues baixar e colocar como "por")
* LANGUAGE_CODE: Idioma do sistema (Default='pt-br')
* TIME_ZONE: Time zone (Default='America/Sao_Paulo')

#### 4.1 Preparação e treinametno da rede YOLO
Primeiramente separe todas as imagens que farão parte do dataset em uma pasta. A primeira etapa será configurar os Bounding Box de cada imagem para identificar as áreas de interesse.
Abra o projeto labelimg e copie as imagens a serem classificadas para a pasta "dataset/imagens". 
<br/>
Copie na sequência o nome das classes em um arquivo txt chamado "classes.txt".
<br/>
Execute o comando > python.exe .\labelImg.py .\dataset\imagens\ .\classes.txt e crie os labels de cada imagem conforme a classe. Para cada imagem será gerado um novo arquivo txt como o nome da imagem e dados dos bounding box gerados.
<br/>
Copie as imagens e seus txts para o projeto principal (VisyonOCR), dividindo eles entre treinamento (conf/yolo_dataset/data/obj) e testes (conf/yolo_dataset/data/valid). Obs: Sugestão de divisão de 80% das imagens para treinamento e 20% para testes/validação.
<br/>
A mesma imagem não pode estar nos dois lugares (treinamento e testes) e não pode haver imagem sem txt com dados de bounding box.
<br/>
Execute o arquivo **processor/util/test_train_generator.py** para criar os arquivos test.txt e train.txt
<br/>
Ajuste o arquivo de configuração do Yolo em conf/yolo_dataset/cfg/yolov4_custom.cfg  para o numero de classes e filtros correspondentes. Abaixo o exemplo para 9 classes:
```  
  #2000 * classes = 2000 * 9 = 18000
  max_batches = 18000
  # 80%/90% max_batches
  # 16000,18000
  # (numero_classes + 5) * 3
  #Os dados abaixo devem ser substituídos nos três pontos da configuração do arquivo de confiuração
  filters=42
  classes=9
  ```
Ajuste os arquivos conf/yolo_dataset/data/obj.data (classes) e conf/yolo_dataset/data/obj.names (nomes das classes: um por linha)
<br/>
Após os passos acima, os arquivos podem ser copiados para o seu google drive e assim permitido que sejam copiados ao google colab e incluídos no darknet para treinamento da rede.
<br/>
Copie a pasta inteira conf/yolo_dataset para o seu Google Drive.
<br/>
Abra o notebook https://colab.research.google.com/drive/1Z2TfoZOjwlpqY-XLRoXvaQH2jWP57zlm?usp=sharing e siga os passos do documento para realizar o treinamento da rede.
<br/>
A rede neural será gerada na pasta yolo_dataset/cnn do Colab após finalizar o treinamento. Copiar ela para a pasta conf/yolo_dataset/cnn do projeto principal com o nome "rede_neural.weights"

### 5. Iniciando o VisyonOCR
Realize a configuração conforme a imagem abaixo:

![runDebugConfiguration.PNG](readmeimg/runDebugConfiguration.PNG)
       

Após a configuração, basta executar o projeto para iniciá-lo.

### 6. Testando a aplicação
A API está disponível através da URL http://localhost:8000/visyonOCR/api/swagger/#/

Usando o Postman os testes poderão ser feitos conforme a imagem abaixo:

1. Falar como usar os filtros e quais filtros disponiveis
2. Falar sobre aplicar escala de cinza 
3. Falar sobre o pre proecssamento e pos processamento
4. Falar como sao apresentados os resultados


















