from max_stack import *


class QueueException(Exception):
    pass


class Queue:
    def __init__(self):
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        return self.s1.is_empty()

    def size(self) -> int:
        return self.s1.size()

    def enqueue(self, value: object) -> None:
        self.s1.push(value)

    def dequeue(self) -> object:
        if self.s1.is_empty():
            raise QueueException(Exception)
        for i in range(self.s1.size()):
            result = self.s1.pop()
            self.s2.push(result)
        self.s2.pop()
        for j in range(self.s2.size()):
            element = self.s2.pop()
            self.s1.push(element)
        return result
