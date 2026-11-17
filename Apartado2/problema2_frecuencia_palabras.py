# Problema 2. Frecuencia de palabras en un texto

def frecuencia_palabras(palabras, ruta_fichero):
    fichero = open(ruta_fichero, "r", encoding="utf-8")
    texto = fichero.read()
    fichero.close()

    # paso todo a minúsculas y quito la puntuación antes de contar,
    # si no "datos," y "datos" serían palabras distintas
    texto = texto.lower()
    signos = ".,;:¿?¡!()\"'«»-"
    for signo in signos:
        texto = texto.replace(signo, " ")
    palabras_texto = texto.split()

    # diccionario: la clave es la palabra y el valor las veces que aparece
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        frecuencias[palabra] = palabras_texto.count(palabra)

    return frecuencias


def mostrar_frecuencias(frecuencias):
    # las enseño ordenadas alfabéticamente por la palabra
    for palabra in sorted(frecuencias):
        print(palabra, "->", frecuencias[palabra])


# Programa de prueba
# hay que ejecutarlo desde la carpeta Apartado2, que es donde está texto_prueba.txt
lista = ["python", "lenguaje", "datos", "modelo", "kaggle", "java"]
resultado = frecuencia_palabras(lista, "texto_prueba.txt")
mostrar_frecuencias(resultado)
