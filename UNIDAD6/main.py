lista_inicial = ['perro', 'elefante', 'dragón']

def lista_recuento_caracteres(lista):
    '''lista_recuento_caracteres: toma una lista de elementos y devuelve una lista con la cantidad de caracteres que le corresponden a cada elemento.

    Args:
        lista (array): lista con elementos de tipo string para contar sus caracteres.
    '''
    lista_nueva = []
    for f in lista:
        lista_nueva.append(len(f))
    
    print(lista_nueva)

# Llamo a la función para ejecutarla al llamar este archivo
lista_recuento_caracteres(lista_inicial)


# Tambien podria haber hecho LISTA POR COMPRENSIÓN
# return print([len(n) for n in lista_inicial])