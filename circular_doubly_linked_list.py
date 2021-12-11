class CDLLException(Exception):
    pass


class DLNode:
    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        return self.sentinel.next == self.sentinel

    def add_front(self, value: object) -> None:
        new = DLNode(value)
        new.next = self.sentinel.next
        self.sentinel.next = new
        new.next.prev = new
        new.prev = self.sentinel

    def add_back(self, value: object) -> None:
        new = DLNode(value)
        cur = self.sentinel.prev
        cur.next = new
        new.next = self.sentinel
        self.sentinel.prev = new
        new.prev = cur

    def insert_at_index(self, index: int, value: object) -> None:
        if (index < 0) or (self.length() < index):
            raise CDLLException(Exception)
        new = DLNode(value)
        cur = self.sentinel
        for i in range(index):
            cur = cur.next
        new.next = cur.next
        cur.next = new
        new.next.prev = new
        new.prev = cur

    def remove_front(self) -> None:
        if self.is_empty():
            raise CDLLException(Exception)
        cur = self.sentinel.next
        self.sentinel.next = cur.next
        cur.next.prev = self.sentinel

    def remove_back(self) -> None:
        if self.is_empty():
            raise CDLLException(Exception)
        cur = self.sentinel.prev
        cur.prev.next = self.sentinel
        self.sentinel.prev = cur.prev

    def remove_at_index(self, index: int) -> None:
        if (index < 0) or (index >= self.length()):
            raise CDLLException(Exception)
        cur = self.sentinel.next
        for i in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def get_front(self) -> object:
        if self.is_empty():
            raise CDLLException(Exception)
        return self.sentinel.next.value

    def get_back(self) -> object:
        if self.is_empty():
            raise CDLLException(Exception)
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        cur = self.sentinel.next
        for i in range(self.length()):
            if cur.value == value:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False

    def count(self, value: object) -> int:
        cur = self.sentinel.next
        count = 0
        for i in range(self.length()):
            if cur.value == value:
                count += 1
            cur = cur.next
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        if (index1 < 0) or (index2 < 0) or (index1 >= self.length()) or (index2 >= self.length()):
            raise CDLLException(Exception)
        one = self.sentinel.next
        two = self.sentinel.next
        for i in range(index1):
            one = one.next
        for i in range(index2):
            two = two.next
        element1 = one.value
        element2 = two.value
        self.remove_at_index(index1)
        self.insert_at_index(index1, two.value)
        self.remove_at_index(index2)
        self.insert_at_index(index2, one.value)

    def reverse(self) -> None:
        count = self.length() - 1
        for i in range(self.length() // 2):
            self.swap_pairs(i, count)
            count -= 1

    def sort(self) -> None:
        sort = True
        while sort:
            n = 0
            cmp = self.sentinel.next
            cur = self.sentinel.next
            for i in range(self.length() - 1):
                if cmp.value > cur.next.value:
                    self.swap_pairs(i, i + 1)
                    n = 1
                    cur = cmp.next
                else:
                    cmp = cmp.next
                    cur = cur.next
            if n == 0:
                sort = False
            
    def rotate(self, steps: int) -> None:
        if (steps == 0) or (self.length() == 0) or ((steps % self.length()) == 0):
            return
        if steps > 0:
            if steps > self.length():
                index = steps % self.length()
            else:
                index = steps
            n = self.length() - index
            head = self.sentinel.next
            tail = self.sentinel
            for i in range(n):
                head = head.next
                tail = tail.next
            if head.value == None:
                head = head.next
            self.sentinel.prev.next = self.sentinel.next
            self.sentinel.next.prev = self.sentinel.prev
            self.sentinel.next = head
            self.sentinel.prev = tail
            head.prev = self.sentinel
            tail.next = self.sentinel
        if steps < 0:
            if (steps * -1) > self.length():
                index = (steps * -1) % self.length()
            else:
                index = steps * -1
            head = self.sentinel.next
            tail = self.sentinel
            for i in range(index):
                head = head.next
                tail = tail.next
            if head.value == None:
                head = head.next
            self.sentinel.prev.next = self.sentinel.next
            self.sentinel.next.prev = self.sentinel.prev
            self.sentinel.next = head
            self.sentinel.prev = tail
            head.prev = self.sentinel
            tail.next = self.sentinel

    def remove_duplicates(self) -> None:
        while True:
            remove = 0
            cur = self.sentinel.next
            for i in range(self.length()):
                if cur.value == cur.next.value:
                    while self.remove(cur.value) == True:
                        remove = 1
                    break
                else:
                    cur = cur.next
            if remove == 0:
                break

    def odd_even(self) -> None:
        cur = self.sentinel.next
        n = self.length() % 2
        for i in range(self.length() // 2):
            element = cur.next.value
            self.add_back(element)
            self.remove_at_index(i + 1)
            cur = self.sentinel.next
            for j in range(i + 1):
                cur = cur.next
