# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
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
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
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
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        new = DLNode(value)
        new.next = self.sentinel.next
        self.sentinel.next = new
        new.next.prev = new
        new.prev = self.sentinel

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        new = DLNode(value)
        cur = self.sentinel.prev
        cur.next = new
        new.next = self.sentinel
        self.sentinel.prev = new
        new.prev = cur

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException(Exception)
        cur = self.sentinel.next
        self.sentinel.next = cur.next
        cur.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException(Exception)
        cur = self.sentinel.prev
        cur.prev.next = self.sentinel
        self.sentinel.prev = cur.prev

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if (index < 0) or (index >= self.length()):
            raise CDLLException(Exception)
        cur = self.sentinel.next
        for i in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException(Exception)
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException(Exception)
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
        cur = self.sentinel.next
        count = 0
        for i in range(self.length()):
            if cur.value == value:
                count += 1
            cur = cur.next
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
        count = self.length() - 1
        for i in range(self.length() // 2):
            self.swap_pairs(i, count)
            count -= 1

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
        cur = self.sentinel.next
        n = self.length() % 2
        for i in range(self.length() // 2):
            element = cur.next.value
            self.add_back(element)
            self.remove_at_index(i + 1)
            cur = self.sentinel.next
            for j in range(i + 1):
                cur = cur.next


if __name__ == '__main__':
    
    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)
    
    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)
    
    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))
    
    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))
    
    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)
    
    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)
    
    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))
    
    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())
    
    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)
    
    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    
    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))
    
    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))
    
    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)
        
    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)
    
    print('\n# reverse example 3')
    
    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age
    
        def __eq__(self, other):
            return self.age == other.age
    
        def __str__(self):
            return str(self.name) + ' ' + str(self.age)
    
    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)
    
    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)
    
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)
    
    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)
    
    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)
    
    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )
    
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)
    
    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )
    
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)
    
