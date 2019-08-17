class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # A] Depth First Search Traversal:
    #       1. In-order Traversal
    #       2. Pre-order Traversal
    #       3. Post-order Traversal
    # B] Breadth First Search Traversal (breadth_first_search.py)

    def inorder_traversal(self):
        if self.root is None:
            return
        else:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.data, end=' ')
            self._inorder_traversal(node.right)

    def preorder_traversal(self):
        if self.root is None:
            return
        else:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is None:
            return
        else:
            self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.data, end=' ')


if __name__ == '__main__':
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(6)
    bst.insert(9)
    bst.insert(3)
    bst.insert(8)

    print('In-Order Traversal -->')
    bst.inorder_traversal()
    print()

    print('Pre-Order Traversal -->')
    bst.preorder_traversal()
    print()

    print('Post-Order Traversal -->')
    bst.postorder_traversal()
