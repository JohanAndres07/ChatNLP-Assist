
vocabulario = {
    "hola": 0, "cómo": 1, "estás": 2, "?": 3, "bien": 4, "gracias": 5, "y": 6, "tú": 7,
    "qué": 8, "haciendo": 9, "ok": 10, "sí": 11, "no": 12, "por": 13, "favor": 14, "buenos": 15,
    "días": 16, "tardes": 17, "noches": 18, "adiós": 19, "nos": 20, "vemos": 21, "luego": 22,
    "mucho": 23, "gusto": 24, "también": 25, "de": 26, "nada": 27, "lo": 28, "siento": 29,
    "perdón": 30, "disculpa": 31, "te": 32, "entiendo": 33, "genial": 34, "claro": 35, "tal": 36,
    "vez": 37, "cuándo": 38, "dónde": 39, "porqué": 40, "para": 41, "quién": 42, "cómo": 43,
    "están": 44, "amigos": 45, "familia": 46, "trabajo": 47, "escuela": 48, "amor": 49, "sí": 50,
    "no": 51, "quiero": 52, "puedo": 53, "voy": 54, "a": 55, "ir": 56, "vengo": 57, "ahora": 58,
    "ya": 59, "aquí": 60, "allá": 61, "bienvenido": 62, "feliz": 63, "triste": 64, "enojado": 65,
    "cansado": 66, "listo": 67, "emocionado": 68, "contento": 69, "aburrido": 70, "llamame": 71,
    "espero": 72, "pronto": 73, "siempre": 74, "nunca": 75, "todos": 76, "cada": 77, "uno": 78,
    "quedamos": 79, "hoy": 80, "mañana": 81, "ayer": 82, "días": 83, "noche": 84, "mundo": 85,
    "vida": 86, "día": 87, "perfecto": 88, "lindo": 89, "bonito": 90, "bello": 91, "feo": 92,
    "amigo": 93, "amiga": 94, "amigos": 95, "familia": 96, "gente": 97, "nuevo": 98, "sueño": 99
}


def tokenizadorSimple(texto):
    return [vocabulario.get(palabra, vocabulario["?"]) for palabra in texto.split()]


vocabularioInvertido = {idx: palabra for palabra, idx in vocabulario.items()}

