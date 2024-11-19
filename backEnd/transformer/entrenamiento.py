# entrenamiento.py
import torch
import torch.nn as nn
import torch.optim as optim
import os
from modelo_transformer import ModeloTransformerSimple
from vocabulario import  tokenizadorSimple
import config  


modelo = ModeloTransformerSimple(config.tamanoVocabulario, config.dimensionEmbeddings, 
                                config.numCabezas, config.dimensionFF, config.longitudMaxima)


if os.path.exists(config.modelo_guardado):
    modelo.load_state_dict(torch.load(config.modelo_guardado))
    modelo.eval()
    print("Modelo cargado exitosamente.")
else:

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(modelo.parameters(), lr=config.learning_rate)


    train_texts = [
    "hola cómo estás?", 
    "cómo estás hoy?", 
    "hola hola cómo estás", 
    "estás bien tú?", 
    "espero que estés bien", 
    "qué planes tienes para hoy?", 
    "cómo va todo?", 
    "me alegra verte", 
    "tienes alguna novedad?", 
    "hoy es un buen día", 
    "espero que tengas un gran día", 
    "qué te parece si nos vemos más tarde?", 
    "estás ocupado ahora?", 
    "hace tiempo que no hablamos", 
    "cuéntame algo interesante", 
    "hola, qué tal?", 
    "todo bien contigo?", 
    "qué tal te fue hoy?", 
    "qué piensas sobre eso?", 
    "me gusta hablar contigo",
    "cuál es tu asignatura favorita?", 
    "has terminado el proyecto?", 
    "qué tema estás estudiando ahora?", 
    "necesitas ayuda con tus deberes?", 
    "qué opinas de este libro?", 
    "vamos a estudiar juntos?", 
    "qué recursos estás usando para aprender?", 
    "cuándo es tu próximo examen?", 
    "qué estrategias usas para memorizar?", 
    "has aprendido algo nuevo hoy?", 
    "cómo organizas tu tiempo de estudio?", 
    "tienes alguna duda sobre el tema?", 
    "qué temas crees que serán difíciles?", 
    "cómo prefieres estudiar, en grupo o solo?", 
    "qué método de estudio te funciona mejor?", 
    "dónde buscas información confiable?", 
    "qué técnicas usas para concentrarte?", 
    "has practicado con ejercicios?", 
    "crees que necesitas más tiempo para prepararte?", 
    "cuál es tu meta para este curso?"
]

    train_tokens = [torch.tensor(tokenizadorSimple(texto)) for texto in train_texts]


    for epoch in range(config.epochs):
        total_loss = 0
        for tokens in train_tokens:
            tokens = tokens.unsqueeze(0) 
            input_ids = tokens[:, :-1]
            target_ids = tokens[:, 1:]
            

            outputs = modelo(input_ids)
            loss = criterion(outputs.view(-1, config.tamanoVocabulario), target_ids.view(-1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch + 1}/{config.epochs}], Loss: {total_loss / len(train_tokens):.4f}")

    torch.save(modelo.state_dict(), config.modelo_guardado)
    print("Modelo entrenado y guardado exitosamente.")
