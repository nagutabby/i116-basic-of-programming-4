class List(object):
    def cons(self, e):
        return None
    def append(self, l):
        return None
    def len(self) -> None | int:
        return None
    def __str__(self) -> str:
        return ''

class Nil(List):
    def cons(self, e):
        return NnList(e, self)
    def append(self, l) -> list:
        return l
    def len(self) -> int:
        return 0
    def __str__(self) -> str:
        return 'nil'

class NnList(List):
    head: int | str | float | None = None
    tail = Nil()
    def __init__(self, h: int | str | float | None, t):
        self.head = h
        self.tail = t
    def cons(self, e):
        return NnList(e, self)
    def append(self, l):
        return NnList(self.head, self.tail.append(l))
    def len(self) -> int:
        return 1 + self.tail.len()
    def __str__(self) -> str:
        return str(self.head) + ' | ' + str(self.tail)
