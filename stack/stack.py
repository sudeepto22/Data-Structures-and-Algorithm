class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.root = None

    def push(self, value) -> None:
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

    def top(self):
        if self.root is not None:
            return self.root.data
        return -1

    def is_empty(self) -> bool:
        if self.root is None:
            return True
        return False

    def print_stack(self) -> None:
        if self.root is None:
            return
        return self._print_stack(self.root)

    def _print_stack(self, node: Node) -> None:
        if node is not None:
            print(node.data, end=' ')
            self._print_stack(node.next)
        else:
            print()


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('Stack -->')
    stack.print_stack()
    print('Top --> '+str(stack.top()))
    print('Stack is empty --> '+str(stack.is_empty()))

