# Problema 3. Trabajo con conjuntos

def operaciones_conjuntos(lista1, lista2):
    # al pasar las listas a conjuntos ya se quitan los repetidos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    resultado = {}
    resultado["interseccion"] = conjunto1.intersection(conjunto2)       # los que están en las dos
    resultado["union"] = conjunto1.union(conjunto2)                     # todos, sin repetir
    resultado["diferencia_simetrica"] = conjunto1.symmetric_difference(conjunto2)  # los que están solo en una
    return resultado


# prueba: el 4 y el 5 están en las dos listas
lista_a = [1, 2, 3, 4, 4, 5]
lista_b = [4, 5, 6, 7, 5]
resultado = operaciones_conjuntos(lista_a, lista_b)
for clave in resultado:
    print(clave, "->", resultado[clave])
