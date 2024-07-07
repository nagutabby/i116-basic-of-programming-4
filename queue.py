class Queue():
    def __init__(self) -> None:
        self.elements: list[int] = []

    def is_empty(self) -> bool:
        if self.elements == []:
            return True
        else:
            return False

    def top(self) -> None | int:
        if self.is_empty():
            return None
        else:
            return self.elements[0]

    def dequeue(self) -> None:
        if not self.is_empty():
            self.elements = self.elements[1:]

    def enqueue(self, e: int) -> None:
        self.elements = self.elements + [e]

    def str(self) -> str:
        return str(self.elements)

queue: Queue = Queue()
print(queue.str())
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.str())
print(queue.is_empty())
print(queue.top())
queue.dequeue()
print(queue.str())
queue.dequeue()
print(queue.str())
