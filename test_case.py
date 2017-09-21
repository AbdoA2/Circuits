import pytest
from Circuit import *
from Element import *


def test_Acircuit1():
	#frequency of circuit = 4
    circuit = ACircuit(4)
    '''
    AC 4
    R_1 v1 v2 60
	C_1 v2 v0 0.01
	I_1 v2 v0 5
	Vsrc_1 v1 v0 20 -15
    '''
    circuit.components = [
        Resistor(1, 2, 60, "R_1"),
        Capacitor(2, 0, 0.01, "C_1", 4),
        Inductor(2, 0, 5, "I_1", 4),
        Vsrc_AC(1, 0, 20, "Vsrc_1", -15)
    ]
    circuit.nodes_count = 2
    circuit.vsrc_count = 1
    currents, voltages = circuit.getElementsCurrents()
    expected_currents = {'C_1': -0.188668500394659+0.6595395607944592j, 'Vsrc_1': -0.04716712509866472+0.16488489019861483j, 'R_1': 0.04716712509866478-0.16488489019861483j, 'I_1': 0.23583562549332374-0.8244244509930739j}
    expected_voltages = {'C_1': 16.48848901986148+4.716712509866475j, 'Vsrc_1': 19.318516525781366-5.176380902050415j, 'R_1': 2.8300275059198867-9.89309341191689j, 'I_1': 16.48848901986148+4.716712509866475j}
    print (currents)
    print (expected_currents)
    print ('-------------------')
    print (voltages)
    print (expected_voltages)
    assert currents == expected_currents
    assert voltages == expected_voltages

test_Acircuit1()