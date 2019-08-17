class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            root_node = self.root
            self.root = Node(value)
            self.root.next = root_node

    def pop(self):
        if self.root is None:
            return
        pop_data = self.root.data
        self.root = self.root.next
        return pop_data

    def print_stack(self):
        if self.root is None:
            return
        return self._print_stack(self.root)

    def _print_stack(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._print_stack(node.next)


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('Stack -->')
    stack.print_stack()
