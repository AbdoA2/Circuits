import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Element import *
from Circuit import *
from CircuitReader import CircuitReaderWriter
import unittest

class TestCircuitReader(unittest.TestCase):
    def test_circuit1(self):
        reader = CircuitReaderWriter()
        self.assertRaises(SyntaxError, reader.readCircuitFromFile, "t1-error.txt")

    def test_circuit2(self):
        reader = CircuitReaderWriter()
        circuit = reader.readCircuitFromFile("t3.txt")
        self.assertEqual(circuit.nodes_count, 4)
        self.assertEqual(circuit.vsrc_count, 2)