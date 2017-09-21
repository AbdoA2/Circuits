import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Element import *
from Circuit import *
import unittest


class TestDCSlover(unittest.TestCase):
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

    def test_circuit2(self):
        circuit = DCircuit()
        circuit.components = [
            Isrc(0, 1, 3, "Isrc_1"),
            Resistor(2, 1, 4, "R_1"),
            Resistor(2, 0, 3, "R_2"),
            Resistor(3, 2, 4, "R_3"),
            Vsrc(3, 0, 12, "Vsrc_1"),
            Vsrc(3, 4, 24, "Vsrc_2"),
            Resistor(4, 1, 8, "R_4")
        ]
        circuit.nodes_count = 4
        circuit.vsrc_count = 2
        currents, voltages = circuit.getElementsCurrents()
        expected_currents = {'Vsrc_2': -2.5, 'R_1': -0.5, 'Isrc_1': 3.0, 'R_2': 2.0, 'R_4': -2.5, 'R_3': 1.5, 'Vsrc_1': 1.0}
        expected_voltages = {'Vsrc_2': 24.0, 'R_1': -2.0, 'Isrc_1': -8.0, 'R_2': 6.0, 'R_4': -20.0, 'R_3': 6.0, 'Vsrc_1': 12.0}
        self.assertDictEqual(currents, expected_currents)
        self.assertDictEqual(voltages, expected_voltages)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDCSlover)
    runner = unittest.TextTestRunner()
    runner.run(suite)