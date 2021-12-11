from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        self.da = DynamicArray()

        # populate bag with initial values
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


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
