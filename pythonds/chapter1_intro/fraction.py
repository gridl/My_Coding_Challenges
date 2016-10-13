
class Fraction:
    def __init__(self, top, bottom):
        if not type(top) == int:
            raise TypeError("Numerator must be an integer")
        elif not type(bottom) == int:
            raise TypeError("Denumerator must be an integer")
        common = self._gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def _gcd(self, num, den):
        while num%den != 0:
            oldnum = num
            oldden = den

            num = oldden
            den = oldnum%oldden
        return den

    def __add__(self, fract2):
        newnum = self.num * fract2.den + self.den * fract2.num
        newden = self.den * fract2.den
        return Fraction(newnum, newden)

    def __iadd__(self, fract2):
        newnum = self.num * fract2.den + self.den * fract2.num
        newden = self.den * fract2.den
        return Fraction(newnum, newden)

    def __sub__(self, fract2):
        newnum = self.num * fract2.den - self.den * fract2.num
        newden = self.den * fract2.den
        return Fraction(newnum, newden)

    def __mul__(self, fract2):
        newnum = self.num * fract2.num
        newden = self.den * fract2.den
        return Fraction(newnum, newden)

    def __truediv__(self, fract2):
        newnum = self.num * fract2.den
        newden = self.den * fract2.num
        return Fraction(newnum, newden)

    def __eq__(self, fract2):
        num1 = self.num * fract2.den
        num2 = fract2.num * self.den

        return num1 == num2

    def __gt__(self, fract2):
        num1 = self.num * fract2.den
        num2 = fract2.num * self.den

        return num1 > num2

    def __ge__(self, fract2):
        num1 = self.num * fract2.den
        num2 = fract2.num * self.den

        return num1 >= num2

    def __lt__(self, fract2):
        num1 = self.num * fract2.den
        num2 = fract2.num * self.den

        return num1 < num2

    def __le__(self, fract2):
        num1 = self.num * fract2.den
        num2 = fract2.num * self.den

        return num1 <= num2

    def __repr__(self):
        return "Fraction(numerator, denumenator)"

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

f1 = Fraction(1, 4)
f2 = Fraction(2, 5)
print(f1 + f2)
print(f1 - f2)
print(f1 > f2)
print(f1 >= f2)
print(f1 < f2)
print(f1 <= f2)
print(f1 == f2)
