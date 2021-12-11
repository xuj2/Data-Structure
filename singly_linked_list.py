class SLLException(Exception):
    pass


class SLNode:
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        return self.head.next == self.tail

    def add_front(self, value: object) -> None:
        new = SLNode(value)
        new.next = self.head.next
        self.head.next = new

    def add_back(self, value: object) -> None:
        new = SLNode(value)
        cur = self.head
        while True:
            if cur.next == self.tail:
                break
            else:
                cur = cur.next
        cur.next = new
        new.next = self.tail

    def insert_at_index(self, index: int, value: object) -> None:
        if (index < 0) or (self.length() < index):
            raise SLLException(Exception)
        new = SLNode(value)
        cur = self.head
        for i in range(index):
            cur = cur.next
        new.next = cur.next
        cur.next = new

    def remove_front(self) -> None:
        if self.is_empty():
            raise SLLException(Exception)
        cur = self.head.next
        self.head.next = cur.next
        

    def remove_back(self) -> None:
        if self.is_empty():
            raise SLLException(Exception)
        prev = self.head
        cur = self.head.next
        while True:
            if cur.next == self.tail:
                break
            else:
                cur = cur.next
                prev = prev.next
        prev.next = self.tail
        

    def remove_at_index(self, index: int) -> None:
        if (index < 0) or (index >= self.length()):
            raise SLLException(Exception)
        prev = self.head
        cur = self.head.next
        for i in range(index):
            cur = cur.next
            prev = prev.next
        prev.next = cur.next

    def get_front(self) -> object:
        if self.is_empty():
            raise SLLException(Exception)
        return self.head.next.value

    def get_back(self) -> object:
        if self.is_empty():
            raise SLLException(Exception)
        cur = self.head
        while True:
            if cur.next == self.tail:
                break
            else:
                cur = cur.next
        return cur.value

    def remove(self, value: object) -> bool:
        prev = self.head
        cur = self.head.next
        for i in range(self.length()):
            if cur.value == value:
                break
            else:
                cur = cur.next
                prev = prev.next
        if cur.value == value:
            prev.next = cur.next
            return True
        return False

    def count(self, value: object) -> int:
        cur = self.head.next
        count = 0
        for i in range(self.length()):
            if cur.value == value:
                count += 1
            cur = cur.next
        return count

    def slice(self, start_index: int, size: int) -> object:
        if (start_index < 0) or (start_index >= self.length()) or (size < 0) or ((start_index + size) > self.length()):
            raise SLLException(Exception)
        newllist = LinkedList()
        cur = self.head.next
        for i in range(start_index):
            cur = cur.next
        for j in range(size):
            newllist.add_back(cur.value)
            cur = cur.next
        return newllist
