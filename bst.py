"""Binary Search Tree implementation keyed by student register number."""
class Node:
    def __init__(self, key, record):
        self.key, self.record = key, record
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, record):
        key = record["reg_no"]
        if self.root is None:
            self.root = Node(key, record)
            return
        cur = self.root
        while True:
            if key == cur.key:
                cur.record = record
                return
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key, record)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(key, record)
                    return
                cur = cur.right

    def search(self, key):
        comparisons, cur = 0, self.root
        while cur:
            comparisons += 1
            if key == cur.key:
                return cur.record, comparisons
            cur = cur.left if key < cur.key else cur.right
        return None, comparisons

    def height(self):
        def h(node):
            if node is None: return 0
            return 1 + max(h(node.left), h(node.right))
        return h(self.root)

    def inorder(self):
        out = []
        def walk(node):
            if node:
                walk(node.left); out.append(node.record); walk(node.right)
        walk(self.root)
        return out
