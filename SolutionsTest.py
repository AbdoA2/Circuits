import unittest
from Circuit import *
from Element import *


class SolutionsTests(unittest.TestCase):
    def test_circuit1(self):
        circuit = DCircuit()
        circuit.components = [
            Isrc(1, 0, 1, "Isrc_1"),
            Resistor(1, 0, 2, "R_1"),
            Resistor(1, 2, 0.5, "R_2"),
            Vsrc(1, 2, 2, "Vsrc_1"),
            Resistor(2, 0, 2, "R_3")
        ]
        circuit.nodes_count = 2
        circuit.vsrc_count = 1
        currents, voltages = circuit.getElementsCurrents()
        expected_currents = {'Vsrc_1': -4.0, 'Isrc_1': 1.0, 'R_3': 0.0, 'R_2': 4.0, 'R_1': 1.0}
        expected_voltages = {'Vsrc_1': 2.0, 'Isrc_1': 2.0, 'R_3': 0.0, 'R_2': 2.0, 'R_1': 2.0}
        self.assertDictEqual(currents, expected_currents)
        self.assertDictEqual(voltages, expected_voltages)
