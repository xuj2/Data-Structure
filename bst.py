# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            self.root = TreeNode(value)
        else:
            cur = self.root
            while True:
                parent = cur
                if value < cur.value:
                    cur = cur.left
                    if cur == None:
                        cur = TreeNode(value)
                        parent.left = cur
                        return
                else:
                    cur = cur.right
                    if cur == None:
                        cur = TreeNode(value)
                        parent.right = cur
                        return
            

    def contains(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return False
        cur = self.root
        while True:
            if cur.value == value:
                return True
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
            if cur == None:
                return False

    def get_first(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return None
        return self.root.value

    def remove_first(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return False
        if self.root.right != None:
            if self.root.right.left == None:
                self.root.right.left = self.root.left
                self.root = self.root.right
                return True
            else:
                cur = self.root.right
                parentS = None
                s = None
                while cur != None:
                    if cur.left != None:
                        parentS = cur
                        s = cur.left
                    cur = cur.left
                s.left = self.root.left
                if s != self.root.right:
                    parentS.left = s.right
                    s.right = self.root.right
                self.root = s
                return True
        else:
            self.root = self.root.left
            return True

    def remove(self, value) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return False
        node = None
        parentNode = None
        s = None
        parentS = None
        cur = self.root
        while node == None:
        #finding node and its parent
            if cur == None:
                return False
            if cur.value == value:
                node = cur
            else:
                if value < cur.value:
                    parentNode = cur
                    cur = cur.left
                else:
                    parentNode = cur
                    cur = cur.right
        if parentNode == None:
            return self.remove_first()
        if (node.left == None) and (node.right == None):
        #delete node straight up
            if node.value < parentNode.value:
                parentNode.left = None
            else:
                parentNode.right = None
        elif (node.left != None) and (node.right == None):
        #right side empty
            if node.value < parentNode.value:
                parentNode.left = node.left
            else:
                parentNode.right = node.left
        elif (node.left == None) and (node.right.left == None):
            if node.value < parentNode.value:
                parentNode.left = node.right
            else:
                parentNode.right = node.right
        else:
            cur = node.right
            while cur != None:
                if cur.left != None:
                    parentS = cur
                    s = cur.left
                cur = cur.left
            if s == None:
                s = node.right
                if s.value < parentNode.value:
                    parentNode.left = s
                else:
                    parentNode.right = s
                s.left = node.left
                none = None
                return True
            else:
                s.left = node.left
            if s != node.right:
                parentS.left = s.right
                s.right = node.right
            if s.value < parentNode.value:
                parentNode.left = s
            else:
                parentNode.right = s
        node = None
        return True

    def pre_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return Queue()
        q = Queue()
        self.prefunc(self.root, q)
        return q

    def prefunc(self, cur, q):
        if cur == None:
            return
        q.enqueue(cur.value)
        self.prefunc(cur.left, q)
        self.prefunc(cur.right, q)

    def in_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        q = Queue()
        if self.root == None:
            return q
        self.infunc(self.root, q)
        return q

    def infunc(self, cur, q):
        if cur == None:
            return
        self.infunc(cur.left, q)
        q.enqueue(cur.value)
        self.infunc(cur.right, q)

    def post_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        q = Queue()
        if self.root == None:
            return q
        self.postfunc(self.root, q)
        return q

    def postfunc(self, cur, q):
        if cur == None:
            return
        self.postfunc(cur.left, q)
        self.postfunc(cur.right, q)
        q.enqueue(cur.value)

    def by_level_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        q = Queue()
        result = Queue()
        q.enqueue(self.root)
        while q.is_empty() == False:
            node = q.dequeue()
            if node != None:
                result.enqueue(node.value)
                q.enqueue(node.left)
                q.enqueue(node.right)
        return result

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return True
        return self.fullfunc(self.root)

    def fullfunc(self, cur):
        if cur == None:
            return True
        elif (cur.left == None) and (cur.right == None):
            return True
        elif (cur.left != None) and (cur.right == None):
            return False
        elif (cur.left == None) and (cur.right != None):
            return False
        else:
            return self.fullfunc(cur.left) and self.fullfunc(cur.right)
        

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return True
        index = 0
        size = self.size()
        return self.completefunc(self.root, index, size)
        
    def completefunc(self, cur, index, size):
        if cur == None:
            return True
        elif index >= size:
            return False
        else:
            left = 2 * index + 1
            right = 2 * index + 2
            return self.completefunc(cur.left, left, size) and self.completefunc(cur.right, right, size)

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return True
        level = 0
        cur = self.root
        while cur.left != None:
            level += 1
            cur = cur.left
        cur = self.root
        for i in range(level):
            if cur.right != None:
                cur = cur.right
            else:
                return False
        return self.is_complete()
            
    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        q = self.pre_order_traversal()
        count = 0
        while q.is_empty() == False:
            q.dequeue()
            count += 1
        return count

    def height(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return -1
        elif (self.root.left == None) and (self.root.right == None):
            return 0
        else:
            count = self.heightfunc(self.root)
            return count - 1
        
    def heightfunc(self, cur):
        if cur == None:
            return 0
        else:
            left = self.heightfunc(cur.left)
            right = self.heightfunc(cur.right)
            if (left > right):
                return left + 1
            else:
                return right + 1

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return 0
        count = self.leavesfunc(self.root)
        return count

    def leavesfunc(self, cur):
        count = 0
        if cur == None:
            return 0
        if (cur.left == None) and (cur.right == None):
            return 1
        else:
            count += self.leavesfunc(cur.left)
            count += self.leavesfunc(cur.right)
        return count

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root == None:
            return 0
        q = self.in_order_traversal()
        count = 1
        cur = q.dequeue()
        while q.is_empty() == False:
            cmp = q.dequeue()
            if cur != cmp:
                count += 1
            cur = cmp
        return count


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    '''
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)
    
    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))
    
    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)
    
    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())
    '''
    tree = BST(["QA","IH","I","HI","L","RK","YX","Z","YX"])
    print(tree.remove("YX"))
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    
    '''
    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    
    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())
    
    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')
    '''
