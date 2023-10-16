class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        raise KeyError(f"Key '{key}' not found")

# Example usage:
separate_chain_table = SeparateChainingHashTable(11)
separate_chain_table.insert("apple", 5)
separate_chain_table.insert("banana", 7)
separate_chain_table.insert("cherry", 10)
print(separate_chain_table.get("banana"))  # Output: 7
