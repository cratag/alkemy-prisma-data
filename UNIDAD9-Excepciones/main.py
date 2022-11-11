'''
Utilizando los conceptos aprendidos en el módulo 9 - Manejo de
excepciones, resolver el siguiente ejercicio.

Dada una lista con diferentes medios de transporte, diseñar una
función solicite el número de índice de la lista y que imprima por
pantalla el texto. En caso de que se genere una excepción, solicitar
nuevamente el número de índice (advirtiendo que se ingresó un valor
incorrecto).

medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ]
'''

def medios_transporte_excepcion() -> str:
    '''This method takes no arguments. User must input an integer after called and returns the conveyance that corresponds to the selected position.

    Args:
        position (num): The position of the conveyance.

    Returns:
        String: The name of the conveyance.
    '''

    # Raise exception if user input is not an integer and call the method again.
    print("Ingresa un número y presiona enter:")
    try:
        position = int(input())
    except Exception:
        print("Valor incorrecto. Ingresa un NUMERO entero por favor.")
        return medios_transporte_excepcion()
        
    MEDIOS_TRANSPORTE = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ]

    try:
        print(MEDIOS_TRANSPORTE[position])
    except IndexError:
        print("Error crítico: ingresa un número dentro del rango 0-4.")
    except Exception as e:
        print("Ocurrió un error al ejecutar.", e)


medios_transporte_excepcion()