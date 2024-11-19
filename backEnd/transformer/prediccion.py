
import torch
from modelo_transformer import ModeloTransformerSimple
from vocabulario import vocabulario, tokenizadorSimple, vocabularioInvertido
import config  


modelo = ModeloTransformerSimple(config.tamanoVocabulario, config.dimensionEmbeddings, 
                                config.numCabezas, config.dimensionFF, config.longitudMaxima)


modelo.load_state_dict(torch.load(config.modelo_guardado))
modelo.eval()
print("Modelo cargado exitosamente.")


textoEntrada = "hola"  

idsEntrada = torch.tensor([tokenizadorSimple(textoEntrada)])

salidaModelo = modelo(idsEntrada)


topk_values, topk_indices = torch.topk(salidaModelo[:, -1, :], 3, dim=-1) 


topk_palabras = [vocabularioInvertido[idx.item()] for idx in topk_indices[0]]

print("Las 3 palabras más probables:", topk_palabras)

