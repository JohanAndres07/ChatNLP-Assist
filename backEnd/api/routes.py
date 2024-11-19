from flask import Blueprint, jsonify, request
import json
import torch
from transformer.modelo_transformer import ModeloTransformerSimple
from transformer.vocabulario import tokenizadorSimple, vocabularioInvertido
import transformer.config as config

api_routes = Blueprint('api_routes', __name__)

texto_entrada_global = None

def load_db():
    try:
        with open('data/messages.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"chat": {"participants": [], "messages": [], "unread_count": {}}}  

def save_db(data):
    with open('data/messages.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  

@api_routes.route('/messages', methods=['GET'])
def get_messages():
    db = load_db()
    return jsonify(db)

@api_routes.route('/messages', methods=['POST'])
def add_message():
    try:
        data = request.get_json()  
        sender = data.get("sender")
        receiver = data.get("receiver")
        message = data.get("message")

        if not sender or not receiver or not message:
            return jsonify({"error": "Missing required fields: sender, receiver, message"}), 400

        db = load_db()

        if sender not in db["chat"]["participants"] or receiver not in db["chat"]["participants"]:
            return jsonify({"error": "Sender or receiver is not a valid participant"}), 400

        new_message = {
            "id": len(db["chat"]["messages"]) + 1,
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "status": "unread"
        }

        db["chat"]["messages"].append(new_message)
        db["chat"]["unread_count"][receiver] = db["chat"]["unread_count"].get(receiver, 0) + 1

        save_db(db)

        return jsonify(new_message), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route('/messages/read', methods=['POST'])
def mark_messages_as_read():
    try:
        data = request.get_json()  
        receiver = data.get("receiver")

        if not receiver:
            return jsonify({"error": "Missing required field: receiver"}), 400

        db = load_db()

        if receiver not in db["chat"]["participants"]:
            return jsonify({"error": "Receiver is not a valid participant"}), 400

        unread_messages = [
            message for message in db["chat"]["messages"]
            if message["receiver"] == receiver and message["status"] == "unread"
        ]

        for message in unread_messages:
            message["status"] = "read"

        db["chat"]["unread_count"][receiver] = 0

        save_db(db)

        return jsonify({"message": f"Marked {len(unread_messages)} messages as read for {receiver}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route('/messages/unread', methods=['GET'])
def get_unread_count():
    db = load_db()
    return jsonify(db["chat"]["unread_count"])

@api_routes.route('/messages/unread', methods=['PATCH'])
def update_unread_count():
    try:
        new_data = request.get_json() 
        db = load_db()

        for user, count in new_data.items():
            if user in db["chat"]["unread_count"]:
                db["chat"]["unread_count"][user] = count
            else:
                return jsonify({"error": f"User {user} not found"}), 400
        
        save_db(db)

        return jsonify({"message": "Unread count updated successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

modelo = None

try:
    modelo = ModeloTransformerSimple(config.tamanoVocabulario, config.dimensionEmbeddings, 
                                    config.numCabezas, config.dimensionFF, config.longitudMaxima)
    modelo.load_state_dict(torch.load(config.modelo_guardado))
    modelo.eval()
    print("Modelo cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")


@api_routes.route('/procesar_texto', methods=['POST'])
def procesar_texto():
    global texto_entrada_global 
    if modelo is None:
        return jsonify({"error": "Modelo no cargado correctamente"}), 500

    try:
        texto_entrada = request.get_json().get("texto")

        if not texto_entrada:
            return jsonify({"error": "Texto no proporcionado"}), 400

        texto_entrada_global = texto_entrada

        ids_entrada = torch.tensor([tokenizadorSimple(texto_entrada)])
        salida_modelo = modelo(ids_entrada)

        topk_values, topk_indices = torch.topk(salida_modelo[:, -1, :], 3, dim=-1)
        topk_palabras = [vocabularioInvertido.get(idx.item(), "Palabra desconocida") for idx in topk_indices[0]]

        return jsonify({"texto_entrada": texto_entrada, "top_3_palabras": topk_palabras}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_routes.route('/obtener_salida', methods=['GET'])
def obtener_salida():
    if modelo is None:
        return jsonify({"error": "Modelo no cargado correctamente"}), 500

    try:

        if texto_entrada_global is None:
            return jsonify({"error": "No se ha procesado ningún texto aún"}), 400

        ids_entrada = torch.tensor([tokenizadorSimple(texto_entrada_global)])
        salida_modelo = modelo(ids_entrada)

        if salida_modelo is None or salida_modelo.size(0) == 0:
            return jsonify({"error": "No se ha procesado ningún texto aún"}), 400

        if salida_modelo.ndimension() < 2:
            return jsonify({"error": "La salida del modelo no tiene la forma esperada"}), 400

        topk_values, topk_indices = torch.topk(salida_modelo[:, -1, :], 4, dim=-1)
        
        topk_palabras = [vocabularioInvertido.get(idx.item(), "Palabra desconocida") for idx in topk_indices[0]]

        return jsonify({"top_3_palabras": topk_palabras}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500