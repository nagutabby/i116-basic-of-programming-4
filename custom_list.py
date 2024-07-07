from __future__ import annotations

class List():
    def cons(self, e: int) -> None | NnList:
        pass
    def append(self, l: NnList) -> None | NnList:
        pass
    def len(self) -> None | int:
        pass
    def __str__(self) -> str:
        return ""

class Nil(List):
    def cons(self, e: int) -> NnList:
        return NnList(e, self)
    def append(self, l: NnList) -> NnList:
        return l
    def len(self) -> int:
        return 0
    def __str__(self) -> str:
        return 'nil'

class NnList(List):
    def __init__(self, head: int, tail: NnList | Nil) -> None:
        self.head = head
        self.tail = tail
    def cons(self, e: int) -> NnList:
        return NnList(e, self)
    def append(self, l: NnList) -> NnList:
        return NnList(self.head, self.tail.append(l))
    def len(self) -> int:
        return 1 + self.tail.len()
    def __str__(self) -> str:
        return f'{self.head} | {self.tail}'
