'''
Utilizando los conceptos aprendidos en el módulo 10 - Testing,
resolver el siguiente ejercicio.
Desarrollar un archivo Python llamado “calculadora.py” y dentro del
mismo desarrollar las siguientes funciones.
- Sumar
- Restar
- Multiplicar
- Dividir

Luego, desarrollar un test utilizando Unittest con tres pruebas para
cada una de las funciones.

Estructurar el proyecto de la siguiente manera:

Calculadora
|------- funciones.py
|------- test_calculadora.py

'''
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# ¿POR QUE ESPECIFICO EL VALOR DE RETORNO SI PY NO LO RESPETA?
def sumar(*args):
    """This functions sums all numbers passed as arguments.

    Args:
        *args: Variable length argument list (numbers only).

    Returns:
        Float of sum of numbers.
    """
    try:
        value = 0
        for n in args:
            value += n
        logging.info(f"SUMA: {value}")
        return value
    except TypeError:
        logging.critical('No se pudo sumar. Los valores deben ser numéricos.')
        raise TypeError
    except Exception as e:
        logging.critical(f'Error de cómputo: {e}')

def restar(*args) -> float:
    """This functions substracts all numbers passed as arguments.

    Args:
        *args: Variable length argument list (numbers only).

    Returns:
        Float of substract of numbers.
    """
    try:
        value = 0
        for n in args:
            value -= n
        logging.info(f"RESTA: {value}")
        return value
    except TypeError:
        logging.critical('ERROR CRITICO: No se pudo restar. Los valores deben ser numéricos.')
        raise TypeError
    except Exception as e:
        logging.critical(f'ERROR CRITICO: {e}')

def multiplicar(*args) -> float:
    """This functions multiplies all numbers passed as arguments.

    Args:
        *args: Variable length argument list (numbers only).

    Returns:
        Float of multiplication of numbers.    
    """
    try:
        value = 1
        for n in args:
            # Verify that each argument is numeric. Otherwise, raise an exception.
            if type(n) != int and type(n) != float: 
                raise TypeError
            value *= n
        logging.info(f"MULTIPLICACIÓN: {value}")
        return value
    except TypeError:
        logging.critical('ERROR CRITICO: No se pudo multiplicar. Los valores deben ser numéricos.')
        raise TypeError
    except Exception as e:
        logging.critical(f'ERROR CRITICO: {e}')

def dividir(*args) -> float:
    """This functions divides all numbers passed as arguments.

    Args:
        *args: Variable length argument list (numbers only).

    Returns:
        Float division of numbers.
    """
    try:
        for nx, n in enumerate(args):
            if nx == 0:
                value = n
            else:
                value /= n
        logging.info(f"DIVISIÓN: {value}")
        return value
    except TypeError:
        logging.critical('ERROR CRITICO: No se pudo dividir. Los valores deben ser numéricos.')
        raise TypeError
    except UnboundLocalError:
        logging.critical('ERROR CRITICO: Divisón vacía. Ingrese un número.')
    except ZeroDivisionError:
        logging.critical('ERROR CRITICO: No se puede dividir por cero.')
        raise ZeroDivisionError
    except Exception as e:
        logging.critical(f'ERROR CRITICO: {type(e)}')
