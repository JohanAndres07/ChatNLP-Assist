# modelo_transformer.py
import torch
import torch.nn as nn

class ModeloTransformerSimple(nn.Module):
    def __init__(self, tamanoVocabulario, dimensionEmbeddings, numCabezas, dimensionFF, longitudMaxima, dropout=0.1):
        super(ModeloTransformerSimple, self).__init__()
        self.embeddings = nn.Embedding(tamanoVocabulario, dimensionEmbeddings)
        self.positionalEmbeddings = nn.Embedding(longitudMaxima, dimensionEmbeddings)
        self.bloqueTransformer = BloqueTransformer(dimensionEmbeddings, numCabezas, dimensionFF, dropout)
        self.capaSalida = nn.Linear(dimensionEmbeddings, tamanoVocabulario)

    def forward(self, entrada):
        posiciones = torch.arange(0, entrada.size(1)).unsqueeze(0).expand(entrada.size(0), entrada.size(1)).to(entrada.device)
        entrada = self.embeddings(entrada) + self.positionalEmbeddings(posiciones)
        salida = self.bloqueTransformer(entrada)
        logits = self.capaSalida(salida)
        return logits

class BloqueTransformer(nn.Module):
    def __init__(self, dimensionEmbeddings, numCabezas, dimensionFF, dropout):
        super(BloqueTransformer, self).__init__()
        self.atencion = nn.MultiheadAttention(dimensionEmbeddings, numCabezas, dropout=dropout)
        self.feedForward = nn.Sequential(
            nn.Linear(dimensionEmbeddings, dimensionFF),
            nn.ReLU(),
            nn.Linear(dimensionFF, dimensionEmbeddings),
        )
        self.normalizacion1 = nn.LayerNorm(dimensionEmbeddings)
        self.normalizacion2 = nn.LayerNorm(dimensionEmbeddings)
        self.dropout = nn.Dropout(dropout)

    def forward(self, entrada):
        salidaAtencion, _ = self.atencion(entrada, entrada, entrada)
        entrada = self.normalizacion1(entrada + self.dropout(salidaAtencion))
        salidaFeedForward = self.feedForward(entrada)
        salidaFinal = self.normalizacion2(entrada + self.dropout(salidaFeedForward))
        return salidaFinal