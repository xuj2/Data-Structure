from dynamic_array import *


class StackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.da = DynamicArray()

    def __str__(self) -> str:
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        return self.da.is_empty()

    def size(self) -> int:
        return self.da.length()

    def push(self, value: object) -> None:
        self.da.append(value)

    def pop(self) -> object:
        if (self.is_empty()):
            raise StackException(Exception)
        value = self.da.get_at_index(self.size() - 1)
        self.da.remove_at_index(self.size() -1)
        return value

    def top(self) -> object:
        if (self.is_empty()):
            raise StackException(Exception)
        value = self.da.get_at_index(self.size() - 1)
        return value
