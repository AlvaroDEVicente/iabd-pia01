# Problema 1. Procesamiento de una lista de enteros

def procesar_lista(numeros):
    # primero me quedo solo con los que no son negativos (el 0 lo dejo)
    sin_negativos = []
    for numero in numeros:
        if numero >= 0:
            sin_negativos.append(numero)

    # quito los repetidos: solo lo añado si todavía no está en la lista
    sin_repetidos = []
    for numero in sin_negativos:
        if numero not in sin_repetidos:
            sin_repetidos.append(numero)

    # y al final los ordeno de menor a mayor
    sin_repetidos.sort()
    return sin_repetidos


# pruebo con el ejemplo del enunciado, tiene que salir [2, 3, 4]
print(procesar_lista([4, -1, 2, 4, 3, -5, 2]))
