#VisyonOCR
O VisyonOCR é um sistema em python que combina técnicas de processamento de imagens, redes YOLO (You Only Look Once) e Reconhecimento Óptico de Caracteres (OCR) para oferecer uma solução completa de extração de texto em imagens.

#Versão
1.0

#Instalando o VisyonOCR pelo Git
git clone https://github.com/libgit2/libgit2

#Ferramenta de Desenvolvimento Utilizada
PyCharm 2024.1 (Community Edition)

#Tesseract
Linux
--sudo add-apt-repository ppa:deadsnakes/ppa -y
--sudo add-apt-repository ppa:deadsnakes/nightly -y
--sudo apt update
--sudo apt install python3.10
--python3.10 --version
--sudo apt install python3.10-dev libpq-dev

--Instalando o tesseract
--sudo apt install tesseract-ocr
--sudo apt install libtesseract-dev
--sudo apt-get install tesseract-ocr-por

Windows
https://github.com/UB-Mannheim/tesseract/wiki

Baixando a linguagem portugues
https://github.com/tesseract-ocr/tessdata/tree/3.04.00
Colocar em tessdata

#Principais Bibliotecas do Python
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

#Projeto para definição das áreas de interesse (Bounding Box)
https://github.com/HumanSignal/labelImg

#Google Colab - Treinamento da Rede Yolo
https://colab.research.google.com/drive/1Z2TfoZOjwlpqY-XLRoXvaQH2jWP57zlm

#Ferramenta de Testes (API)
https://www.postman.com/

-----------------

#Configurando o Projeto
Abra o arquivo main/settings.py e realize a configuração dos principais pontos do sistema:
PATH_URL= Nome do projeto quando for realizada a execução (Default: visyonOCR)
WINDOWS= Se True indicará que o SO utilizado é Windows. Se False Linux (Default False)
EXIBIR_IMAGENS_MD= Irá exibir as imagens no processo de identificação (Default False)
CNN_MIN_PREDICTION= Previsão mínima para rede YOLO considerar a predição (Default= 0.70 )
pytesseract.pytesseract.tesseract_cmd= Local onde o Tesseract está instalado (Default= r"/usr/bin/tesseract")
TESSERACT_LANGUAGE=Idioma do Tesseract (Default= "eng", para portugues baixar e colocar como "por")
LANGUAGE_CODE= Idioma do sistema (Default='pt-br')
TIME_ZONE= Time zone (Default='America/Sao_Paulo')

#PREPARAÇÃO E TREINAMENTO DA REDE YOLO.
Primeiramente separe todas as imagens que farão parte do dataset em uma pasta. A primeira etapa será configurar os Bounding Box de cada imagem para identificar as áreas de interesse.
Abra O PROJETO labelimg e copie as imagens a serem classificadas para a pasta dataset/imagens. Copie na sequencia as classes em um arquivo txt chamado classes.txt.
Executar o comando > python.exe .\labelImg.py .\dataset\imagens\ .\classes.txt e crie os labels de cada imagem conforme a classe. Para cada imagem será gerado um novo arquivo txt como o nome da imagem e dados dos bounding box gerados.
Copie as imagens e seus txts para o projeto principal (VisyonOCR), dividindo eles entre treinamento (conf/yolo_dataset/data/obj) e testes (conf/yolo_dataset/data/valid). (Sugestão de divisão de 80% das imagens para treinamento e 20% para testes).
A mesma imagem não pode estar nos dois lugares e não pode haver imagem sem txt.
Execute o arquivo processor/util/test_train_generator.py para criar os arquivos test.txt e train.txt
Ajuste o arquivo de configuração do Yolo em conf/yolo_dataset/cfg/yolov4_custom.cfg  para o numero de classes e filtros correspondentes. Abaixo o exemplo para 9 classes:
  # 2000 * classes = 2000 * 9 = 18000
  max_batches = 18000
  # 80%/90% max_batches
  # 16000,18000
  # (numero_classes + 5) * 3
  #Os dados abaixo devem ser substituídos em três pontos da configuração
  filters=42
  classes=9
Ajuste os arquivos conf/yolo_dataset/data/obj.data (classes) e conf/yolo_dataset/data/obj.names (nomes das classes: um por linha)
Após os passos acima, os arquivos podem ser copiados para o seu google drive e assim permitido que sejam copiados ao google colab e incluídos no darknet para treinamento da rede.
Copie a pasta inteira conf/yolo_dataset para o seu Google Drive.
Abra o notebook https://colab.research.google.com/drive/1Z2TfoZOjwlpqY-XLRoXvaQH2jWP57zlm e siga os passos do documento para treinamento da rede.
A rede neural será gerada na pasta yolo_dataset/cnn do Colab após finalizar o treinamento. Copiar ela para a pasta conf/yolo_dataset/cnn do projeto principal com o nome "rede_neural.weights"

#Iniciando o VisyonOCR
Realize a configuração conforme a imagem abaixo

Após a configuração, basta executar o projeto para iniciá-lo.

#Testando a aplicação
A API está disponível através da URL http://localhost:8000/visyonOCR/api/swagger/#/
Usando o Postman os testes poderão ser feitos:
























FLUXO COMPLETO

1 FLUXO DE TREINAMENTO (DEMORADO)
SISTEMA CARREGA O PDF
SISTEMA TRANSFORMA O PDF EM IMAGENS (1 POR PAGÍNA)
SISTEMA TRANSFORMA A IMAGEM EM ESCALA DE CINZA
PARA CADA IMAGEM O SISTEMA APLICA O PreProcessamentoAgrupadoThreadProcessor QUE RESULTARA EM INUMERAS IMAGENS CONFORME O ArrayProcessamentoPermutacaoSimples
COM OS RESULTADOS SALVAR EM BANCO DE DADOS A IMAGEM ORIGINAL EM UMA TABELA, COM O GRAU DE SIMILARIDADE, E EM TABELA RELACIONADA AS IMAGENS RESULTANTES COM SEUS RESPECTIVOS FILTROS APLICADOS (METRICAS)
APLICAR OCR E CNN PARA CADA IMAGEM RESULTANTE E SALVAR OS RESULTADOS REFERENTES (QTDADE PALAVRAS TEXTO, QTDADE PALAVRAS REQUISITADAS, TAXA TERMOS, ETC...)
APAGAR TODAS AS IMAGENS TRATADAS PARA NAO OCUPAR ESPAÇO EM BANCO


2 FLUXO DE IDENTIFICAÇÃO (RÁPIDO SE ENCONTRADA SIMILARIDADE)
SISTEMA CARREGA O PDF
SISTEMA TRANSFORMA O PDF EM IMAGENS (1 POR PAGÍNA)
SISTEMA TRANSFORMA A IMAGEM EM ESCALA DE CINZA
PARA CADA IMAGEM DO PDF O SISTEMA BUSCA UMA IMAGEM DE TREINAMENTO PREVIAMENTE REALIZADA POR SIMILARIDADE COM INFORMADA
SE NAO ENCONTRAR A SIMILARIDADE EXECUTA O PASSO 1 (FLUXO DE TREINAMENTO) E SALVA NOVA SIMILARIDADE
SE ENCONTRAR A SIMILARIDADE O SISTEMA BUSCA NA IMAGEM SIMILAR A IMAGEM RESULTANTE COM MELHOR RESULTADO E APLICA OS MESMOS PARAMETROS USADOS NA IMAGEM DO PDF
SISTEMA APLICA OCR E CNN E RETIRA O TEXTO DA IMAGEM
SISTEMA TENTA ENCONTRAR OS DADOS DO DEPÓSITO, COMO ID E CONTA (EX: BUSCA POR OEPRAÇÃO 040) E PROCESSO
SISTEMA SALVA NA TABELA DE RESULTADO A IMAGEM, DADOS DE IDENTIFICAÇÃO DO PDF, PROCESSO, TEXTO TOTAL ENCONTRADO E DADOS FILTRADOS (CONTA, AGENCIA, IDENTIFICADOR) ETC..


FLUXO DO SISTEMA
IMPORTAR O DOCUMENTO
QUARTZ QUE INICIA O PROCESSAMENTO DE DOCUMENTOS PENDENTES
CONVERTE O DOCUMENTO EM IMAGENS
PROCESSA AS IMAGENS APLICANDO OS FILTROS
SALVA AS IMAGENS COM FILTROS
PROCESSA AS IMAGENS COM FILTROS APLICANDO OCR E CNN
SALVA OS RESULTADOS DE OCR E CNN NAS IMAGENS COM FILTROS
PROCESSA OS RESULTADOS DE OCR E CNN E ATRIBUI O RESULTADO FINAL DE VALIDAÇÃO
APAGA AS IMAGENS PARA EVITAR SOBRECARGA NO BANCO DE DADOS





--COMO GERAR O DATASET, TREINAR A REDE NEURAL USANDO YOLO E GERAR O ARQUIVO DE CLASSIFICAÇÃO PARA APLICAÇÃO EM PYTHON

1. Separar os documentos PDFs em uma pasta, criar dentro da pasta de documentos uma pasta img.
2. Executar o arquivo conf/util/convert_pdf2img.py para converter todos os PDFs em imagens na pasta img acima criada
3. Separar as imagens dentro de subpastas nas subclasses necessárias (Cada subpasta é uma classe de imagem)
4. Duplicar o diretorio criado das imagens separadas em classes (um para TF e outro para o YOLO

Preparando o dataset do TF
1. Analisr o diretorio TF de todas as subclasses e converter as imagens em paisagem para retrato
2. Copiar as imagens com suas classes (pastas) para o projeto principal em conf/data_original/data_original
3. Executar o arquivo conf/util/resise_img.py para conversao das imagens a um tamanho padrao da rede neural

Treinando a rede em TF
1. Na classe TFModels poderão ser criados os modelos da CNN
2. A classe TensorFlowTEST inicia o treinamento da rede, podendo ser configurado o numero de epocas e tamanho do batch de processamento
3. Após o treinamento a rede neural e a estatística de treinamento serão criadas em conf/tf_dataset/cnn

Preparando e Treinando a rede em YOLO
1. Configurar os boundi boxes de cada imagem do diretório Yolo
2. Paar isso ABRIR O PROJETO labelimg (Novo projeto python)
3. Copiar as imagens a serem classificadas para a pasta dataset/imagens
4. Copiar as classes em um arquivo txt chamado classes.txt
5. Executar > python.exe .\labelImg.py .\dataset\imagens\ .\classes.txt
6. Criar os labels de cada imagem conforme a classe
7. Após copiar os arquivos e seus txts para o projeto principal, dividindo eles entre treinamento (yolo_dataset/data/obj) 80% e testes (yolo_dataset/data/valid) 20%. A mesma imagem não pode estar nos dois lugares e não pode haver imagem sem txt
8. Executar o arquivo conf/util/gerar_test.py e conf/util/gerar_train.py para criar os arquivos text.txt e train.txt
9. Ajustar o arquivo de configuração do Yolo em yolo_dataset/cfg/yolov4_custom.cfg  para o numero de classes e filtros correspondentes. Abaixo o exemplo para 9 classes:
  # 2000 * classes = 2000 * 9 = 18000
  max_batches = 18000
  # 80%/90% max_batches
  # 16000,18000
  # (numero_classes + 5) * 3
  #Os dados abaixo devem ser substituídos em três pontos da configuração
  filters=42
  classes=9
10. Ajustar os arquivos yolo_dataset/data/obj.data (classes) e yolo_dataset/data/obj.names (nomes das classes um em cada linha)
11. Após os passos acima, os arquivos podem ser copiados para o google drive e assim permitido que sejam copiados ao google colab e incluídos no darknet para treinamento da rede
12. Seguir os passos presentes no colab no arquivo 'SEPZ YOLOv4 - Treinamento do detector.ipynb'
13. A rede neural será gerada na pasta yolo_dataset/cnn do Colab. Copiar ela para a pasta conf/yolo_dataset/cnn do projeto principal