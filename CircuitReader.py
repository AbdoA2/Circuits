from Circuit import *
from Element import *
from Matrix import *
import os
import sys
import re


class CircuitReaderWriter:

    def readCircuitFromFile(self, filename):
        file = open(filename)

        circuitParams = file.readline().split()
        if circuitParams[0] == 'AC' and circuitParams[1].isnumeric() and len(circuitParams) == 2:
            circuit = self.__readAC(file.readlines(), float(circuitParams[1]))
        elif circuitParams[0] == 'DC' and len(circuitParams) == 1:
            circuit = self.__readDC(file.readlines())
        else:
            raise SyntaxError("Can't determine circuit type")
        return circuit



    def parseCircuitFromString(self, circuitString):
        i = circuitString.index('\n')
        circuitParams = circuitString[:i].split()
        if circuitParams[0] == 'AC':
            circuit = self.__readAC(circuitString[i+1:].split('\n'), float(circuitParams[1]))
        else:
            circuit = self.__readDC(circuitString[i+1:].split('\n'))

        return circuit

    def writeCircuitToFile(self, circuit, filename):
        file = open(filename, 'w+')
        file.write(str(circuit) + '\n')

    def __readDC(self, lines):
        pattern = re.compile("(R|Vsrc|Isrc|C|I)_[\d]+[\s]+v[\d]+[\s]+v[\d]+[\s]+[\d]+[\.]{0,1}[\d]*")
        elements = {'Isrc': Isrc, 'Vsrc': Vsrc, 'R':Resistor, 'I':Inductor, 'C':Capacitor}
        circuit = DCircuit()
        j = 2
        for line in lines:
            if len(line) < 1:
                continue
            if not pattern.match(line):
                raise SyntaxError("Syntax error at line " + str(j))
            attrs = line.split()
            posNode = int(attrs[1][1:])
            negNode = int(attrs[2][1:])
            value = float(attrs[3])
            i = attrs[0].index('_')
            element = elements[attrs[0][:i]](posNode, negNode, value, attrs[0])
            circuit.addComponent(element)
            j += 1
        return circuit

    def __readAC(self, lines, omega):
        circuit = ACircuit(omega)
        j = 2
        for line in lines:
            try:
                if len(line) < 1:
                    continue
                attrs = line.split()
                posNode = int(attrs[1][1:])
                negNode = int(attrs[2][1:])
                value = float(attrs[3])
                i = attrs[0].index('_')
                elementType = attrs[0][:i]
                if elementType == 'Isrc':
                    circuit.addComponent(Isrc_AC(posNode, negNode, value, attrs[0], float(attrs[4])))
                elif elementType == 'Vsrc':
                    circuit.addComponent(Vsrc_AC(posNode, negNode, value, attrs[0], float(attrs[4])))
                elif elementType == 'R':
                    circuit.addComponent(Resistor(posNode, negNode, value, attrs[0]))
                elif elementType == 'C':
                    circuit.addComponent(Capacitor(posNode, negNode, value, attrs[0], omega))
                else:
                    circuit.addComponent(Inductor(posNode, negNode, value, attrs[0], omega))
                j += 1
            except:
                print("Syntax error at line %d." % j)
                raise SyntaxError

        return circuit


if __name__ == "__main__":
    reader = CircuitReaderWriter()
    c1 = reader.readCircuitFromFile(sys.argv[1])
    print(c1.getElementsVoltages())
    print(c1.getElementsCurrents())
    #print(c1)

'''
m1 = c1.getCircuitMatrix()
x = m1.solve()
print(m1)
print(x)
'''
