from Element import *
from Matrix import *
import unittest

class VsrcTest(unittest.TestCase):
    def setUp(self):
        self.vsrc = Vsrc(1, 0, 10, "Vsrc_1")
        self.A = Matrix(3, 4)

    def test_str(self):
        "str"
        self.assertEqual(str(self.vsrc), "Vsrc_1 v1 v0 10.0000")

    def test_addStamp(self):
        "addStamp"
        self.vsrc.addStamp(self.A.matrix, 2, 1)
        self.assertEqual(self.A.matrix[0][2], 1)
        self.assertEqual(self.A.matrix[2][0], 1)
        self.assertEqual(self.A.matrix[2][3], complex(10, 0))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")

