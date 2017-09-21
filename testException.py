import unittest


def div(a, b):
    return a / b


class TestException(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 0

    def test_division(self):
        self.assertRaises(ZeroDivisionError, div, self.a, self.b)

    def tearDown(self):
        print("Division test ended")