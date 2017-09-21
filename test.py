import unittest


class TestBasicMethods(unittest.TestCase):
    def setUp(self):
        if self.shortDescription() == "upper":
            self.text = "computer engineering"
        elif self.shortDescription() == "isupper":
            self.text = "COMPUTER"
        else:
            self.text = "hello world"

    def test_upper(self):
        "upper"
        self.assertEqual(self.text.upper(), 'COMPUTER ENGINEERING')

    def test_isupper(self):
        "isupper"
        self.assertTrue(self.text.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        "spilt"
        self.assertEqual(self.text.split(), ['hello', 'world'])

    def tearDown(self):
        print(self.shortDescription() + " test has ended")

class TestClassMethods(unittest.TestCase):
    a = 100
    b = 200

    @classmethod
    def setUpClass(cls):
        cls.text = "The British Empire is the largest on in the history"

    @unittest.expectedFailure
    def test_findFrance(self):
        self.assertGreaterEqual(TestClassMethods.text.find("France"), 0)

    @unittest.skip("Just skip this test")
    def test_multiply(self):
        self.assertEqual(TestClassMethods.a * TestClassMethods.b, 20000)

    @unittest.skipIf(a < b, "Skip if a < b")
    def test_less(self):
        self.assertLess(TestClassMethods.a, TestClassMethods.b)

    @classmethod
    def tearDownClass(cls):
        print("\nTestClassMethods testes has ended")

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestBasicMethods("test_isupper"))
    return test_suite

# if __name__ == '__main__':
#     #unittest.main()
#     # runner = unittest.TextTestRunner()
#     # result = runner.run(suite())
#     # print(result.failures)
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicMethods)
#     unittest.TextTestRunner(verbosity=2).run(suite)
#
