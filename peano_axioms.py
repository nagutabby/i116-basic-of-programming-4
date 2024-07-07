from __future__ import annotations

class NaturalNumber():
    def plus(self, y: Zero | NonZeroNaturalNumber) -> None | int | Zero | NonZeroNaturalNumber:
        pass
    def multiply(self, y) -> None | Zero | NonZeroNaturalNumber:
        pass
    def str(self) -> None | str:
        pass

class Zero(NaturalNumber):
    def plus(self, y: Zero | NonZeroNaturalNumber):
        return y
    def multiply(self, y: int) -> Zero:
        return self
    def str(self) -> str:
        return '0'

class NonZeroNaturalNumber(NaturalNumber):
    def __init__(self, prev: Zero | NonZeroNaturalNumber) -> None:
        self.prev = prev
    def plus(self, y: Zero | NonZeroNaturalNumber) -> NonZeroNaturalNumber:
        return NonZeroNaturalNumber(self.prev.plus(y))
    def multiply(self, y) -> Zero | NonZeroNaturalNumber:
        return y.plus(self.prev.multiply(y))
    def str(self) -> str:
        return f's({self.prev.str()})'

zero: Zero = Zero()
one: NonZeroNaturalNumber = NonZeroNaturalNumber(zero)
two: NonZeroNaturalNumber = NonZeroNaturalNumber(one)
three: NonZeroNaturalNumber = NonZeroNaturalNumber(two)
four: NonZeroNaturalNumber = NonZeroNaturalNumber(three)
print('zero: ', zero.str())
print('one: ', one.str())
print('two: ', two.str())
print('three: ', three.str())
print('four: ', four.str())
print(three.str(), '+', four.str(), ' = ', three.plus(four).str())
print(three.str(), '*', two.str(), ' = ', three.multiply(two).str())
