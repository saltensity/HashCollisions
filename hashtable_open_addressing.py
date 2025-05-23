class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None]*size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """Computes and returns the initial location for a given key using built-in hash function"""
        return hash(key) % self.size
      
    def _rehash(self, old_location: int) -> int:
        """ Compute and returns the next location for linear probing """
        return (old_location + 1) % self.size

    def setitem(self, key: str, value: dict) -> None:
        """
        Sets the value associated with the key in the Hash Table.
        """
        location = self._hash(key)
        for _ in range(self.size):
          if self.values[location] is None or self.values[location][0] == key:
            self.values[location] = (key, value)
            return
          
          location = self._rehash(location)
        
        raise Exception("Table is full!")

    def getitem(self, key: str) -> 'dict | None':
        """
        Gets the value associated with the key in the Hash Table.
        """
        location = self._hash(key)
        for _ in range(self.size):
          if self.values[location] is not None and self.values[location][0] == key:
            return self.values[location][1]
          
          location = self._rehash(location)
        
        raise KeyError()
    
    def delitem(self, key: str) -> None:
        """
        Deletes the matching key-value pair in the Hash Table.
        """
        location = self._hash(key)
        for _ in range(self.size):
          if self.values[location] is not None and self.values[location][0] == key:
            self.values[location] = None
            return
          
          location = self._rehash(location)
        
        raise KeyError()
