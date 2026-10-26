# Desafio 93

traducciones = {
    "hello": {
        "es": "hola",
        "fr": "bonjour",
        "pt": "olá",
        "it": "ciao",
        "de": "hallo"
    },
    "world": {
        "es": "mundo",
        "fr": "monde",
        "pt": "mundo",
        "it": "mondo",
        "de": "Welt"
    },
    "book": {
        "es": "libro",
        "fr": "livre",
        "pt": "livro",
        "it": "libro",
        "de": "Buch"
    },
    "friend": {
        "es": "amigo",
        "fr": "ami",
        "pt": "amigo",
        "it": "amico",
        "de": "Freund"
    }
}


def traducir(palabra, idiomas):
    resultado = {}

    for idioma in idiomas:
        if palabra in traducciones and idioma in traducciones[palabra]:
            resultado[idioma] = traducciones[palabra][idioma]
        else:
            resultado[idioma] = "Traducción no encontrada"

    return resultado


print(traducir("hello", ["es", "it", "de"]))
print(traducir("book", ["fr", "pt"]))
print(traducir("house", ["es", "de"]))