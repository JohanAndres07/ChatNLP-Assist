import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'transformer')))
from vocabulario import vocabulario


tamanoVocabulario = len(vocabulario)
dimensionEmbeddings = 64
numCabezas = 4
dimensionFF = 128
longitudMaxima = 10
epochs = 50

learning_rate = 0.0001
modelo_guardado = 'transformer\modelo_transformer.pth'
