import os
import sys
import unittest

# sys.path.append('')
sys.path.append('../')
from pathlib import Path

from docs_from_tests.instrument_call_hierarchy import (
    finalise_call_hierarchy, initialise_call_hierarchy,
    instrument_and_import_package)

import functions.functions as f

# Imports para configurar docs_from_tests


instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'functions'), 'functions')

class MyTest(unittest.TestCase):
    def test_hello_world(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        # Palabra a testear
        to_check = "hola mundo"
        
        valid_world = f.get_valid_word()
        self.assertEqual(valid_world, to_check)

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

if __name__ == '__main__':
    unittest.main()
