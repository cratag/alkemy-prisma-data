lista_inicial = ['perro', 'elefante', 'dragón']

def lista_recuento_caracteres(lista):
    # Toma lista de elementos e imprime lista de cantidad de caracteres correspondiente a cada elemento
    lista_nueva = []
    for f in lista:
        lista_nueva.append(len(f))
    
    print(lista_nueva)

# Llamo a la función para ejecutarla al llamar este archivo
lista_recuento_caracteres(lista_inicial)


# Tambien podria haber hecho LISTA POR COMPRENSIÓN
# return print([len(n) for n in lista_inicial])