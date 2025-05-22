class HashTable:
    def __init__(self, size):
        pass

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """Computes and returns the initial location for a given key using built-in hash function"""
        return hash(key) % self.size
      
    def _rehash(self, old_location: int) -> int:
		""" Compute and returns the next location for linear probing """
   		pass

    def setitem(self, key: str, value: dict) -> None:
        """
        """
    	pass

    def getitem(self, key: str) -> 'dict | None':
        """
        """
    	pass