import datetime
import sys
import unittest

sys.path.append('../')
import functions.calculadora as calc


class MyTests(unittest.TestCase):
    # Sum Test Cases
    def test_sum_two_args(self):
        self.assertEqual(calc.sumar(10.5, 20), 30.5)
    def test_sum_four_args(self):
        self.assertEqual(calc.sumar(4, 20.7, 6, 5), 35.7)
    def test_sum_non_numeric(self):
        with self.assertRaises(TypeError):
            calc.sumar(14, "v")

    # Substract Test Cases
    def test_substract_two_args(self):
        self.assertEqual(calc.restar(10, 5), -15)
    def test_substract_four_args(self):
        self.assertEqual(calc.restar(20.30, 5, 10, 5), -40.30)
    def test_substract_non_numeric(self):
        with self.assertRaises(TypeError):
            calc.restar(4, "v")

    # Multiplication Test Cases
    def test_multiplication_two_args(self):
        self.assertEqual(calc.multiplicar(10.1, 5), 50.5)
    def test_multiplication_four_args(self):
        self.assertEqual(calc.multiplicar(2, 5, 10, 2), 200)
    def test_multiplication_non_numeric(self):
        with self.assertRaises(TypeError):
            calc.multiplicar(50, "ups")

    # Division Test Cases
    def test_division(self):
        self.assertEqual(calc.dividir(10, 5), 2)
    def test_division_non_numeric(self):
        with self.assertRaises(TypeError):
            calc.dividir(10, "v")
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.dividir(10, 0)


def insert_header(f):
    f.write('\n')
    f.write('******************TESTING**************************')
    f.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time)
    f.write('\n')
    return f

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)

if __name__ == '__main__':
    with open('../doc/txt/testing.txt', 'w') as f:
        f = insert_header(f)
        main(f)