from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        self.da = DynamicArray()
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        return self.da.length()

    def add(self, value: object) -> None:
        self.da.append(value)

    def remove(self, value: object) -> bool:
        for i in range(self.size()):
            if (self.da.get_at_index(i) == value):
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        count = 0
        for i in range(self.size()):
            if (self.da.get_at_index(i) == value):
                count += 1
        return count

    def clear(self) -> None:
        for i in range(self.size() - 1, -1, -1):
            self.da.remove_at_index(i)

    def equal(self, second_bag: object) -> bool:
        if (self.size() != second_bag.size()):
            return False
        for i in range(self.size()):
            check = False
            for j in range(second_bag.size()):
                bag1 = self.da.get_at_index(i)
                bag2 = second_bag.da.get_at_index(j)
                if bag1 == bag2:
                    check = True
            if check == False:
                    return False
        return True
