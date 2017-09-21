from cmath import rect, polar, pi, phase

class Element:
    def __init__(self, posNode, negNode, value, id):
        self.posNode = posNode
        self.negNode = negNode
        self.value = value
        self.id = id

    # n is the number of nodes, m is the number of independent voltage sources
    def addStamp(self, A, n, m):
        pN = self.posNode - 1
        nN = self.negNode - 1
        if pN >= 0 and nN >= 0:
            A[pN][pN] += 1/self.value
            A[nN][nN] += 1/self.value
            A[nN][pN] -= 1/self.value
            A[pN][nN] -= 1/self.value
        elif pN >= 0:
            A[pN][pN] += 1/self.value
        else:
            A[nN][nN] -= 1/self.value

    def __str__(self):
        return "%s v%d v%d" % (self.id, self.posNode, self.negNode)

class Resistor(Element):
    def __str__(self):
        return super(Resistor, self).__str__() + (" %.4f" % self.value)

class Vsrc(Element):
    def __init__(self, posNode, negNode, value, id, phase=0):
        super(Vsrc, self).__init__(posNode, negNode, value, id)
        self.phase = phase
        self.value = rect(self.value, self.phase * pi/180)

    def addStamp(self, A, n, m):
        pN = self.posNode - 1
        nN = self.negNode - 1
        i = self.id.index('_')
        id = int(self.id[i+1:]) - 1
        if pN >= 0:
            A[pN][n + id] = 1
            A[n + id][pN] = 1
        if nN >= 0:
            A[nN][n + id] = -1
            A[n + id][nN] = -1

        A[n + id][n + m] = self.value

    def __str__(self):
        return super(Vsrc, self).__str__() + (" %.4f" % abs(self.value))

class Vsrc_AC(Vsrc):
    def __init__(self, posNode, negNode, value, id, phase=0):
        super(Vsrc_AC, self).__init__(posNode, negNode, value, id, phase)

    def __str__(self):
        return super(Vsrc_AC, self).__str__() + (" %.4f" % (phase(self.value) * 180/pi))


class Isrc(Element):
    def __init__(self, posNode, negNode, value, id, phase=0):
        super(Isrc, self).__init__(posNode, negNode, value, id)
        self.phase = phase
        self.value = rect(self.value, self.phase * pi/180)

    def addStamp(self, A, n, m):
        pN = self.posNode - 1
        nN = self.negNode - 1
        if pN >= 0:
            A[pN][n + m] -= self.value
        if nN >= 0:
            A[nN][n + m] += self.value

    def __str__(self):
        return super(Isrc, self).__str__() + (" %.4f" % abs(self.value))

class Isrc_AC(Isrc):
    def __init__(self, posNode, negNode, value, id, phase=0):
        super(Isrc_AC, self).__init__(posNode, negNode, value, id, phase)

    def __str__(self):
        return super(Isrc_AC, self).__str__() + (" %.4f" % (phase(self.value) * 180/pi))

class Capacitor(Element):
    def __init__(self, posNode, negNode, value, id, omega=1):
        super(Capacitor, self).__init__(posNode, negNode, value, id)
        self.omega = omega
        self.v = value
        self.value = 1/(self.omega * complex(0, self.value))

    def __str__(self):
        return super(Capacitor, self).__str__() + (" %.4f" %  self.v)


class Inductor(Element):
    def __init__(self, posNode, negNode, value, id, omega=1):
        super(Inductor, self).__init__(posNode, negNode, value, id)
        self.omega = omega
        self.v = value
        self.value = self.omega * complex(0, self.value)

    def __str__(self):
        return super(Inductor, self).__str__() + (" %.4f" %  self.v)