class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            # Linear probing: increment the index by 1
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            # Linear probing: increment the index by 1
            index = (index + 1) % self.size
        raise KeyError(f"Key '{key}' not found")

# Example usage:
linear_probe_table = LinearProbingHashTable(11)
linear_probe_table.insert("apple", 5)
linear_probe_table.insert("banana", 7)
linear_probe_table.insert("cherry", 10)
print(linear_probe_table.get("banana"))  # Output: 7
