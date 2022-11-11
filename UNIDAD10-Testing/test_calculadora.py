# Third party methods.
import unittest

# Local modules.
import calculadora


class TestCalculatorMethods(unittest.TestCase):
    # Sum Test Cases
    def test_sum_two_args(self):
        self.assertEqual(calculadora.sumar(10.5, 20), 30.5)
    def test_sum_four_args(self):
        self.assertEqual(calculadora.sumar(4, 20.7, 6, 5), 35.7)
    def test_sum_non_numeric(self):
        with self.assertRaises(TypeError):
            calculadora.sumar(14, "v")

    # Substract Test Cases
    def test_substract_two_args(self):
        self.assertEqual(calculadora.restar(10, 5), -15)
    def test_substract_four_args(self):
        self.assertEqual(calculadora.restar(20.30, 5, 10, 5), -40.30)
    def test_substract_non_numeric(self):
        with self.assertRaises(TypeError):
            calculadora.restar(4, "v")

    # Multiplication Test Cases
    def test_multiplication_two_args(self):
        self.assertEqual(calculadora.multiplicar(10.1, 5), 50.5)
    def test_multiplication_four_args(self):
        self.assertEqual(calculadora.multiplicar(2, 5, 10, 2), 200)
    def test_multiplication_non_numeric(self):
        with self.assertRaises(TypeError):
            calculadora.multiplicar(50, "ups")

    # Division Test Cases
    def test_division(self):
        self.assertEqual(calculadora.dividir(10, 5), 2)
    def test_division_non_numeric(self):
        with self.assertRaises(TypeError):
            calculadora.dividir(10, "v")
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(10, 0)


# Run tests.
if __name__ == "__main__":
    unittest.main()
