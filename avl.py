"""AVL self-balancing binary search tree keyed by register number."""
class Node:
    def __init__(self, key, record):
        self.key, self.record = key, record
        self.left = self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def _height(self, n):
        return n.height if n else 0

    def _update(self, n):
        n.height = 1 + max(self._height(n.left), self._height(n.right))

    def _balance(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    def _right_rotate(self, y):
        x, t2 = y.left, y.left.right
        x.right, y.left = y, t2
        self._update(y); self._update(x)
        return x

    def _left_rotate(self, x):
        y, t2 = x.right, x.right.left
        y.left, x.right = x, t2
        self._update(x); self._update(y)
        return y

    def _insert(self, node, record):
        key = record["reg_no"]
        if node is None: return Node(key, record)
        if key < node.key: node.left = self._insert(node.left, record)
        elif key > node.key: node.right = self._insert(node.right, record)
        else:
            node.record = record
            return node
        self._update(node)
        balance = self._balance(node)
        if balance > 1 and key < node.left.key: return self._right_rotate(node)       # LL
        if balance < -1 and key > node.right.key: return self._left_rotate(node)      # RR
        if balance > 1 and key > node.left.key:                                      # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:                                    # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def insert(self, record):
        self.root = self._insert(self.root, record)

    def search(self, key):
        comparisons, cur = 0, self.root
        while cur:
            comparisons += 1
            if key == cur.key: return cur.record, comparisons
            cur = cur.left if key < cur.key else cur.right
        return None, comparisons

    def height(self):
        return self._height(self.root)

    def inorder(self):
        out = []
        def walk(node):
            if node:
                walk(node.left); out.append(node.record); walk(node.right)
        walk(self.root)
        return out
