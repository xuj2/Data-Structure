from dynamic_array import *


class QueueException(Exception):
    pass


class Queue:
    def __init__(self):
        self.da = DynamicArray()

    def __str__(self):
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        return self.da.is_empty()

    def size(self) -> int:
        return self.da.length()

    def enqueue(self, value: object) -> None:
        self.da.append(value)

    def dequeue(self) -> object:
        if (self.is_empty()):
            raise QueueException(Exception)
        value = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return value
