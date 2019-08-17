class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.root = None

    def enqueue(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._enqueue(self.root, value)

    def _enqueue(self, node, value):
        if node.next is None:
            node.next = Node(value)
        else:
            self._enqueue(node.next, value)

    def dequeue(self):
        root_node = self.root
        self.root = self.root.next
        return root_node.data

    def print_queue(self):
        if self.root is None:
            return
        else:
            self._print_queue(self.root)

    def _print_queue(self, node):
        if node is not None:
            print(node.data)
            self._print_queue(node.next)


queue = Queue()
for i in range(1, 11):
    queue.enqueue(i)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print('Queue -->')
queue.print_queue()
