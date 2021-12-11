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



if __name__ == "__main__":
    
    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)
    
    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")
    
    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    # remove_at_index - example 2
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)
    
    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")
    
    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)
    
    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    
    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

