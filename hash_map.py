from SLL_DA import *


def hash_function_1(key: str) -> int:
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        buckets = DynamicArray()
        for i in range(self.capacity):
            buckets.append(LinkedList())
        self.buckets = buckets
        self.size = 0

    def get(self, key: str) -> object:
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            for node in ll:
                if node.key == key:
                    return node.value
        return None

    def put(self, key: str, value: object) -> None:
        index = abs(self.hash_function(key)) % self.capacity
        ll = self.buckets.get_at_index(index)
        if ll.length() == 0:
            ll.insert(key, value)
            self.size += 1
            return
        else:
            if ll.contains(key) != None:
                for node in ll:
                    if node.key == key:
                        node.value = value
            else:
                ll.insert(key, value)
                self.size += 1

    def remove(self, key: str) -> None:
        index = abs(self.hash_function(key)) % self.capacity
        ll = self.buckets.get_at_index(index)
        if ll.remove(key):
            self.size -= 1
            

    def contains_key(self, key: str) -> bool:
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            for node in ll:
                if node.key == key:
                    return True
        return False

    def empty_buckets(self) -> int:
        n = 0
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            if ll.length() == 0:
                n += 1
        return n

    def table_load(self) -> float:
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        if new_capacity < 1:
            return
        new_hash = HashMap(new_capacity, self.hash_function)
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            if ll.length() > 0:
                for node in ll:
                    new_hash.put(node.key, node.value)
        self.buckets = new_hash.buckets
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        array = DynamicArray()
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            if ll.length() > 0:
                for node in ll:
                    array.append(node.key)
        return array
