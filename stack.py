from __future__ import annotations

class Stack():
    def push(self, e: int) -> None | NeStack:
        pass
    def pop(self) -> None | EmptyStack | NeStack:
        pass
    def top(self) -> None | int:
        pass
    def __str__(self) -> str:
        return ''

class EmptyStack(Stack):
    def push(self, e: int) -> NeStack:
        return NeStack(e, self)
    def pop(self) -> EmptyStack:
        return self
    def top(self) -> None:
        return None
    def __str__(self):
        return 'empty stack'

class NeStack(Stack):
    def __init__(self, t: int, b: EmptyStack | NeStack) -> None:
        self.top_elt = t
        self.bottom = b
    def push(self, e: int) -> NeStack:
        return NeStack(e, self)
    def pop(self) -> EmptyStack | NeStack:
        return self.bottom
    def top(self) -> int:
        return self.top_elt
    def __str__(self) -> str:
        return f'{self.top_elt} ; {self.bottom}'

s1: EmptyStack = EmptyStack()
s2: NeStack = s1.push(0)
s3: NeStack = s2.push(1)
s4: NeStack = s3.push(2)
print(str(s4))
print(s4.top())
s5 = s4.pop()
print(str(s5))
print(s5.top())
