class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return
    queue = list()
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data)
        pop_node = queue.pop(0)

        if pop_node.left is not None:
            queue.append(pop_node.left)

        if pop_node.right is not None:
            queue.append(pop_node.right)


if __name__ == '__main__':
    node = Node(4)
    node.left = Node(2)
    node.right = Node(5)
    node.left.left = Node(1)
    node.left.right = Node(3)
    node.right.right = Node(6)
    node.right.right.right = Node(9)
    node.right.right.right.left = Node(8)

    bfs(node)
