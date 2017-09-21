from Matrix import Matrix
from cmath import polar
from copy import deepcopy


class Circuit:
    def __init__(self, components=[]):
        self.components = deepcopy(components)
        self.nodes_count = 0
        self.vsrc_count = 0

    def addComponent(self, element):
        self.components.append(element)
        self.nodes_count = max(self.nodes_count, element.posNode, element.negNode)
        if type(element).__name__.startswith('Vsrc'):
            self.vsrc_count += 1


    def getCircuitMatrix(self):
        A = Matrix(self.nodes_count + self.vsrc_count, self.nodes_count + self.vsrc_count + 1)
        for component in self.components:
            component.addStamp(A.matrix, self.nodes_count, self.vsrc_count)
        print(A)
        return A

    def getNodeVoltages(self):
        A = self.getCircuitMatrix()
        x = A.solve()
        return x

    def getElementsVoltages(self):
        x = [0] + self.getNodeVoltages()
        voltages = dict()
        for component in self.components:
            voltages[component.id] = (x[component.posNode] - x[component.negNode])
        return voltages

    def getElementsCurrents(self):
        x = [0] + self.getNodeVoltages()
        currents = dict()
        voltages = dict()
        for component in self.components:
            voltages[component.id] = (x[component.posNode] - x[component.negNode])
            if component.id.startswith('I_') or component.id.startswith('C') or component.id.startswith('R'):
                currents[component.id] = (x[component.posNode] - x[component.negNode]) / component.value
            elif component.id.startswith('Vsrc'):
                currents[component.id] = x[self.nodes_count + int(component.id[5:])]
            else:
                currents[component.id] = component.value
        return currents, voltages

    def __str__(self):
        return "\n".join(str(i) for i in self.components)


class DCircuit(Circuit):
    def getElementsVoltages(self):
        voltages = super(DCircuit, self).getElementsVoltages()
        for k, v in voltages.items():
            voltages[k] = round(v.real, 4)
        return voltages

    def getElementsCurrents(self):
        currents, voltages = super(DCircuit, self).getElementsCurrents()
        for k, v in voltages.items():
            voltages[k] = round(v.real, 4)
        for k, v in currents.items():
            currents[k] = round(v.real, 4)
        return currents, voltages

    def __str__(self):
        return "DC\n" + super(DCircuit, self).__str__()


class ACircuit(Circuit):
    def __init__(self, omega, components=[]):
        super(ACircuit, self).__init__(components)
        self.omega = omega

    def __str__(self):
        return ("AC %d \n" % (self.omega)) + super(ACircuit, self).__str__()

