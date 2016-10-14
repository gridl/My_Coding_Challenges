
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n, pinA=None, pinB=None):
        LogicGate.__init__(self, n)

        self.pinA = pinA
        self.pinB = pinB

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        elif type(self.pinA) == int:
            return self.pinA
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        elif type(self.pinB) == int:
            return self.pinB
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):

    def __init__(self, n,  pin = None):
        LogicGate.__init__(self, n)

        self.pin = pin

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):

    def __init__(self, n, pinA=None, pinB=None):
        BinaryGate.__init__(self, n, pinA, pinB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n, pinA=None, pinB=None):
        BinaryGate.__init__(self, n, pinA, pinB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):

    def __init__(self, n, pin=None):
        UnaryGate.__init__(self, n, pin)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class NorGate(BinaryGate):

    def __init__(self, n, pinA=None, pinB=None):
        BinaryGate.__init__(self, n, pinA, pinB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 1
        else:
            return 0


class NandGate(BinaryGate):

    def __init__(self, n, pinA=None, pinB=None):
        BinaryGate.__init__(self, n, pinA, pinB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):

    def __init__(self, n, pinA=None, pinB=None):
        BinaryGate.__init__(self, n, pinA, pinB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        elif a == 1 and b == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def check_eq(A, B, C, D):
    """
    Create a series of gates that prove the following equality
    NOT (( A and B) or (C and D))
    is that same as
    NOT( A and B ) and NOT (C and D)
    Make sure to use some of your new gates in the simulation.
    """
    g1 = AndGate("G1", A, B)
    g2 = AndGate("G2", C, D)
    g3 = NorGate("G3")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)

    result1 = g3.getOutput()

    g4 = NandGate("G4", A, B)
    g5 = NandGate("G5", C, D)
    g6 = AndGate("G6")

    c3 = Connector(g4,g6)
    c4 = Connector(g5,g6)

    result2 = g6.getOutput()

    return result1 == result2

#print( check_eq(0,0,0,0) )
#print( check_eq(1,0,0,1) )


def half_adder(A, B):

    S = XorGate("G2", A, B).getOutput()
    C = AndGate("G1", A, B).getOutput()

    return S, C

#print("Check half_adder truth table")
#print( half_adder(0,0) == (0,0) )
#print( half_adder(1,0) == (1,0) )
#print( half_adder(0,1) == (1,0) )
#print( half_adder(1,1) == (0,1) )

def full_adder(A, B, Cin):
    pass
