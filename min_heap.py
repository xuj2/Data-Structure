# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            self.heap.append(node)
        else:
            self.heap.append(node)
            index = self.heap.length() - 1
            while index != 0:
                parent_index = ((index - 1) // 2)
                cur = self.heap.get_at_index(index)
                parent = self.heap.get_at_index(parent_index)
                if cur < parent:
                    self.heap.swap(index, parent_index)
                    index = parent_index
                else:
                    return
                

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException(Exception)
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException(Exception)
        value = self.heap.get_at_index(0)
        if self.heap.length() > 1:
            self.heap.swap(0, self.heap.length() - 1)
            self.heap.pop()
        else:
            self.heap.pop()
            return value
        index = 0
        while True:
            if (index * 2 + 1) >= self.heap.length():
                return value
            cur = self.heap.get_at_index(index)
            left = self.heap.get_at_index(index * 2 + 1)
            if (index * 2 + 2) < self.heap.length():
                right = self.heap.get_at_index(index * 2 + 2)
                if left < cur and left <= right:
                    self.heap.swap(index, index * 2 + 1)
                    index = index * 2 + 1
                elif right < cur and right < left:
                    self.heap.swap(index, index * 2 + 2)
                    index = index * 2 + 2
                else:
                    return value
            else:
                if left < cur:
                    self.heap.swap(index, index * 2 + 1)
                return value
        

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            element = da.get_at_index(i)
            self.heap.append(element)
        target = self.heap.length() // 2 - 1
        for i in range(target, -1, -1):
            index = i
            while True:
                if (index * 2 + 1) >= self.heap.length():
                    break
                cur = self.heap.get_at_index(index)
                left = self.heap.get_at_index(index * 2 + 1)
                if (index * 2 + 2) < self.heap.length():
                    right = self.heap.get_at_index(index * 2 + 2)
                    if left < cur and left <= right:
                        self.heap.swap(index, index * 2 + 1)
                        index = index * 2 + 1
                    elif right < cur and right < left:
                        self.heap.swap(index, index * 2 + 2)
                        index = index * 2 + 2
                    else:
                        break
                else:
                    if left < cur:
                        self.heap.swap(index, index * 2 + 1)
                    break


# BASIC TESTING
if __name__ == '__main__':
    
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    
    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
    da = DynamicArray([32, 12, 2, 8, 16, 20, 24, 40, 4])
    h.build_heap(da)
    print(h)
    
