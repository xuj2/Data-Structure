from singly_linked_list import *


class StackException(Exception):
    pass


class MaxStack:
    def __init__(self):
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        return self.sll_val.is_empty()

    def size(self) -> int:
        return self.sll_val.length()

    def push(self, value: object) -> None:
        if self.sll_max.is_empty():
            self.sll_max.add_front(value)
        else:
            copy = self.sll_max.slice(0, self.sll_max.length())
            for i in range(self.sll_max.length()):
                element = copy.get_front()
                copy.remove_front()
                if value < element:
                    self.sll_max.insert_at_index(i, value)
                    break
            if value >= self.sll_max.get_back():
                self.sll_max.add_back(value)
        self.sll_val.add_front(value)

    def pop(self) -> object:
        if self.is_empty():
            raise StackException(Exception)
        element = self.sll_val.get_front()
        self.sll_max.remove(element)
        self.sll_val.remove_front()
        return element

    def top(self) -> object:
        if self.is_empty():
            raise StackException(Exception)
        return self.sll_val.get_front()

    def get_max(self) -> object:
        if self.is_empty():
            raise StackException(Exception)
        return self.sll_max.get_back()
