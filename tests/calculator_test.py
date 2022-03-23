from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('5+4'), 9)

    def test_minus(self):
        self.assertEqual(calculator('5-3'), 2)

    def test_mult(self):
        self.assertEqual(calculator('4*6'), 24)

    def test_devide(self):
        self.assertEqual(calculator('54/9'), 6)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('3 6')
        self.assertEqual('Выражение должно содержать один знак из (+-/*)', e.exception.args[0])

    def test_no_signs_2(self):
        with self.assertRaises(ValueError) as e:
            calculator('2 + 3 + 4')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_no_int(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.6 + 3 ')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])




if __name__ == '__main__':
    main()
