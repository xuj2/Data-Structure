from static_array import *


class DynamicArrayException(Exception):
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        self.size = 0
        self.capacity = 4
        self.first = 0 
        self.data = StaticArray(self.capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        return self.size == 0

    def length(self) -> int:
        return self.size

    def resize(self, new_capacity: int) -> None:
        if (new_capacity <= 0) or (self.length() > new_capacity):
            return
        array = StaticArray(new_capacity)
        for i in range(self.length()):
            array.set(i, self.data.get(i))
        self.data = array
        self.capacity = new_capacity

    def append(self, value: object) -> None:
        if self.capacity == self.length():
            self.resize(self.capacity * 2)
        self.data.set(self.length(), value)
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        if (self.length() < index) or (index < 0):
            raise DynamicArrayException(Exception)
        if self.capacity == self.length():
            self.resize(self.capacity * 2)
        if index == self.length():
            self.data.set(index, value)
        else:
            for i in range(self.length() - 1, index - 1, -1):
                self.data.set((i+1), self.data.get(i))
            self.data.set(index, value)
        self.size += 1

    def get_at_index(self, index: int) -> object:
        if (self.length() <= index) or (index < 0):
            raise DynamicArrayException(Exception)
        return self.data.get(index)

    def remove_at_index(self, index: int) -> None:
        if (self.length() <= index) or (index < 0):
            raise DynamicArrayException(Exception)
        if self.size < (self.capacity / 4):
            if (self.length() * 2) < 10 and (self.capacity > 10):
                self.resize(10)
            elif (self.length() * 2) > 10:
                self.resize(self.length() * 2)
        if self.length() == index:
            self.data.set(index, None)
        else:
            for i in range(index, self.length() - 1):
                self.data.set(i, self.data.get(i + 1))
            self.data.set((self.length() - 1), None)
        self.size -= 1

    def slice(self, start_index: int, quantity: int) -> object:
        if (start_index < 0) or (quantity < 0) or (self.length() < (start_index + quantity)) or (start_index == self.length()):
            raise DynamicArrayException(Exception)
        array = DynamicArray()
        for i in range(start_index, (start_index + quantity)):
            array.append(self.data.get(i))
        return array

    def merge(self, second_da: object) -> None:
        for i in range(second_da.length()):
            self.append(second_da.data.get(i))
        

    def map(self, map_func) -> object:
        array = DynamicArray()
        for i in range(self.length()):
            array.append(map_func(self.data.get(i)))
        return array
            

    def filter(self, filter_func) -> object:
        array = DynamicArray()
        for i in range(self.length()):
            if filter_func(self.data.get(i)) == True:
                array.append(self.data.get(i))
        return array
            

    def reduce(self, reduce_func, initializer=None) -> object:
        if self.is_empty():
            return initializer
        if initializer != None:
            first = initializer
            index = 0
        else:
            first = self.data.get(0)
            index = 1
            if self.length() == 1:
                return first
        for i in range(index, self.length()):
            first = reduce_func(first, self.data.get(i))
        return first
