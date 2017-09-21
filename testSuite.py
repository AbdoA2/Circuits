import unittest

class AdditionTest(unittest.TestCase):
    def setUp(self):
        self.a = 100; self.b = 215

    def runTest(self):
        self.assertEqual(self.a + self.b, 315)

    def tearDown(self):
        print("Addition Test is ended")

class SubtractionTest(unittest.TestCase):
    def setUp(self):
        self.a = 100; self.b = 215

    def runTest(self):
        self.assertEqual(self.a - self.b, -115)

    def tearDown(self):
        print("Subtraction Test is ended")

def suite():
    mathematics_suite = unittest.TestSuite()
    mathematics_suite.addTest(AdditionTest())
    mathematics_suite.addTest(SubtractionTest())
    return mathematics_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
    print("oooo")