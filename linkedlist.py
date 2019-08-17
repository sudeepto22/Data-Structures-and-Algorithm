class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.next is None:
            node.next = Node(value)
        else:
            self._insert(node.next, value)

    def insert_first(self, value):
        root_node = self.root
        self.root = Node(value)
        self.root.next = root_node

    def print_linkedlist(self):
        if self.root is None:
            return
        self._print_linkedlist(self.root)

    def _print_linkedlist(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._print_linkedlist(node.next)


linkedlist = LinkedList()
for i in range(1, 11):
    linkedlist.insert(i)

linkedlist.insert_first(12)
linkedlist.print_linkedlist()
