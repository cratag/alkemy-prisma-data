# Funciones.

def get_hola()-> str:
    '''get_hola: metodo que al llamarlo responde hola.

    Returns:
        str: devuelve 'hola'
    '''
    return 'hola'

def get_mundo ()-> str:
    '''get_mundo metodo que al llamarlo responde mundo

    Returns:
        str: devuelve 'mundo'
    '''
    
    return 'mundo'

def get_valid_word()-> str:
    '''get_valid_word junta los returns de dos metodos y genera una frase completa.

    Returns:
        str: acopla los returns de dos metodos y trae una str final 'hola mundo'
    '''
    valid_word = get_hola() + ' ' + get_mundo()
    return valid_word
