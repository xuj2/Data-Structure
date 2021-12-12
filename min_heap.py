from SLL_DA import *


class MinHeapException(Exception):
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        self.heap = DynamicArray()
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        return self.heap.length() == 0

    def add(self, node: object) -> None:
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
        if self.is_empty():
            raise MinHeapException(Exception)
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
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
