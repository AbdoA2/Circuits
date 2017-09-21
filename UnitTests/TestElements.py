import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Element import *
from Matrix import *
import unittest


class VsrcTest(unittest.TestCase):
    def setUp(self):
        self.vsrc = Vsrc(1, 0, 10, "Vsrc_1")
        self.A = Matrix(3, 4)

    def test_str(self):
        "Voltage Source str"
        self.assertEqual(str(self.vsrc), "Vsrc_1 v1 v0 10.0000")

    def test_addStamp(self):
        "Voltage Source addStamp"
        self.vsrc.addStamp(self.A.matrix, 2, 1)
        self.assertEqual(self.A.matrix[0][2], 1)
        self.assertEqual(self.A.matrix[2][0], 1)
        self.assertEqual(self.A.matrix[2][3], complex(10, 0))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class Vsrc_ACTest(unittest.TestCase):
    def setUp(self):
        self.vsrc = Vsrc_AC(1, 0, 10, "Vsrc_1", 30)
        self.A = Matrix(3, 4)

    def test_str(self):
        "AC Voltage Source str"
        self.assertEqual(str(self.vsrc), "Vsrc_1 v1 v0 10.0000 30.0000")

    def test_addStamp(self):
        "AC Voltage Source addStamp"
        self.vsrc.addStamp(self.A.matrix, 2, 1)
        self.assertEqual(self.A.matrix[0][2], 1)
        self.assertEqual(self.A.matrix[2][0], 1)
        self.assertEqual(self.A.matrix[2][3], complex(8.660254037844387, 4.999999999999999))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class IsrcTest(unittest.TestCase):
    def setUp(self):
        self.isrc = Isrc(1, 0, 10, "Isrc_1")
        self.A = Matrix(2, 3)

    def test_str(self):
        "Current Source str"
        self.assertEqual(str(self.isrc), "Isrc_1 v1 v0 10.0000")

    def test_addStamp(self):
        "Current Source addStamp"
        self.isrc.addStamp(self.A.matrix, 2, 0)
        self.assertEqual(self.A.matrix[0][2], complex(10, 0))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class Isrc_ACTest(unittest.TestCase):
    def setUp(self):
        self.isrc = Isrc_AC(1, 0, 10, "Isrc_1", 30)
        self.A = Matrix(2, 3)

    def test_str(self):
        "AC Current Source str"
        self.assertEqual(str(self.isrc), "Isrc_1 v1 v0 10.0000 30.0000")

    def test_addStamp(self):
        "AC Current Source addStamp"
        self.isrc.addStamp(self.A.matrix, 2, 0)
        self.assertEqual(self.A.matrix[0][2], complex(8.660254037844387, 4.999999999999999))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class ResistorTest(unittest.TestCase):
    def setUp(self):
        self.resistor = Resistor(2, 1, 4, "R_1")
        self.A = Matrix(2, 3)

    def test_str(self):
        "Resistor str"
        self.assertEqual(str(self.resistor), "R_1 v2 v1 4.0000")

    def test_addStamp(self):
        "Resistor addStamp"
        self.resistor.addStamp(self.A.matrix, 2, 0)
        self.assertEqual(self.A.matrix[0][0], self.A.matrix[1][1])
        self.assertEqual(self.A.matrix[0][1], self.A.matrix[1][0])
        self.assertEqual(self.A.matrix[0][0], 0.25)
        self.assertEqual(self.A.matrix[0][1], -0.25)

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class CapacitorTest(unittest.TestCase):
    def setUp(self):
        self.capacitor = Capacitor(2, 1, 0.01, "C_1", 4)
        self.A = Matrix(2, 3)

    def test_str(self):
        "Capacitor str"
        self.assertEqual(str(self.capacitor), "C_1 v2 v1 0.0100")

    def test_addStamp(self):
        "Capacitor addStamp"
        self.capacitor.addStamp(self.A.matrix, 2, 0)
        self.assertEqual(self.A.matrix[0][0], self.A.matrix[1][1])
        self.assertEqual(self.A.matrix[0][1], self.A.matrix[1][0])
        self.assertEqual(self.A.matrix[0][0], complex(0, 0.04))
        self.assertEqual(self.A.matrix[0][1], complex(0, -0.04))


    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")


class InductorTest(unittest.TestCase):
    def setUp(self):
        self.inductor = Inductor(2, 1, 5, "R_1", 4)
        self.A = Matrix(2, 3)

    def test_str(self):
        "Inductor str"
        self.assertEqual(str(self.inductor), "R_1 v2 v1 5.0000")

    def test_addStamp(self):
        "Inductor addStamp"
        self.inductor.addStamp(self.A.matrix, 2, 0)
        self.assertEqual(self.A.matrix[0][0], self.A.matrix[1][1])
        self.assertEqual(self.A.matrix[0][1], self.A.matrix[1][0])
        self.assertEqual(self.A.matrix[0][0], complex(0, -0.05))
        self.assertEqual(self.A.matrix[0][1], complex(0, 0.05))

    def tearDown(self):
        print("Test " + self.shortDescription() + " has ended")

