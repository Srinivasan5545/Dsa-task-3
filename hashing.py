"""Hash table using open addressing and linear probing."""
class LinearProbingHash:
    def __init__(self, capacity=53):
        self.capacity = capacity
        self.table = [None] * capacity
        self.total_collisions = 0

    def _hash(self, key):
        return key % self.capacity

    def insert(self, record):
        key = record["reg_no"]
        index = self._hash(key)
        collisions = 0
        for _ in range(self.capacity):
            slot = self.table[index]
            if slot is None:
                self.table[index] = (key, record)
                self.total_collisions += collisions
                return collisions
            if slot[0] == key:
                self.table[index] = (key, record)
                self.total_collisions += collisions
                return collisions
            collisions += 1
            index = (index + 1) % self.capacity
        raise OverflowError("Hash table is full")

    def search(self, key):
        index = self._hash(key)
        comparisons = 0
        for _ in range(self.capacity):
            slot = self.table[index]
            if slot is None:
                return None, comparisons
            comparisons += 1
            if slot[0] == key:
                return slot[1], comparisons
            index = (index + 1) % self.capacity
        return None, comparisons

    def collision_count(self):
        return self.total_collisions
