import unittest

class Calculator:
    def add(self, a, b):
        return a + b


class Example(unittest.TestCase):
    def test_add1Plus1(self):
        calc = Calculator()
        self.assertEquals(calc.add(1, 1), 2)
    def test_add2Plus1(self):
        # arrange
        calc = Calculator()
        # act
        res = calc.add(2, 1)
        # assert
        self.assertEquals(res, 3)

if __name__ == '__main__':
    unittest.main()