import os
import sys
import unittest

# sys.path.append('')
sys.path.append('../')
from pathlib import Path

import functions.calculadora as f
from docs_from_tests.instrument_call_hierarchy import (
    finalise_call_hierarchy, initialise_call_hierarchy,
    instrument_and_import_package)

# Imports para configurar docs_from_tests -- ¿ POR QUE SIN ESTO NO MUESTRA NADA EL DIAGRAMA ?
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'functions'), 'functions')

class MyTest(unittest.TestCase):
    def test_sums(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        # Sum Test Cases
        # self.assertEqual(f.sumar(10.5, 20), 30.5)
        # self.assertEqual(f.sumar(4, 20.7, 6, 5), 35.7)
        with self.assertRaises(TypeError):
            f.sumar(14, "v")

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagramas', 'Sumas - diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_substractions(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        # Substract Test Cases
        self.assertEqual(f.restar(10, 5), -15)
        self.assertEqual(f.restar(20.30, 5, 10, 5), -40.30)
        with self.assertRaises(TypeError):
            f.restar(4, "v")

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagramas', 'Restas - diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_divisions(self):
        
        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        # Division Test Cases
        self.assertEqual(f.dividir(10, 5), 2)
        with self.assertRaises(TypeError):
            f.dividir(10, "v")
        with self.assertRaises(ZeroDivisionError):
            f.dividir(10, 0)

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagramas', 'Divisiones - diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_multiplies(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        # Multiplication Test Cases
        self.assertEqual(f.multiplicar(10.1, 5), 50.5)
        self.assertEqual(f.multiplicar(2, 5, 10, 2), 200)
        with self.assertRaises(TypeError):
            f.multiplicar(50, "ups")

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagramas', 'Multiplicaciones - diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

        
if __name__ == '__main__':
    unittest.main()

