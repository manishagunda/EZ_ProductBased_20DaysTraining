class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        i = 0
        while self.table[index] is not None:
            # Quadratic probing: increment the index by i^2
            index = (index + i**2) % self.size
            i += 1
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            # Quadratic probing: increment the index by i^2
            index = (index + i**2) % self.size
            i += 1
        raise KeyError(f"Key '{key}' not found")

# Example usage:
quadratic_probe_table = QuadraticProbingHashTable(11)
quadratic_probe_table.insert("apple", 5)
quadratic_probe_table.insert("banana", 7)
quadratic_probe_table.insert("cherry", 10)
print(quadratic_probe_table.get("cherry"))  # Output: 10
