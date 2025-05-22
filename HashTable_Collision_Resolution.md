## Hash Table (Collision Resolution) Practice

In the last session, we implemented a **Hash Table**, the backbone of which is the **hash function**.

An **ideal hash function** gives a **unique location for each key**. **However**, since the number of possible keys is much larger than the number of locations, **some keys** will inevitably **hash to the same index location**. When this happens, it is called a **hash collision**.

### Collision Resolution (Open Addressing)
For this exercise, we will attempt collision resolution using **Open Addressing**. Refer to your notes if you would like to learn about the other collision resolution strategy, using **Closed Addressing**.

Some of the **open addressing strategies** include:
- **Linear Probing** (we will be using this today)
- Quadratic Probing (not in syllabus)
-  Double Hashing (not in syllabus)
-  Robin Hood Hashing (not in syllabus)

### Task (Linear Probing)
With reference to the **algorithm** given in the [notes](https://docs.google.com/document/d/18-ROQl3yrCsoCzIDRKCvKqx82IprpE5UoxTVyPfw8bo/edit?tab=t.0#heading=h.ue8zij3d9n9u), you are required to Implement a **Hash Table** class (in the **hashtable_open_addressing.py file**) that **incorporates open addressing collision resolution**, using **Linear Probing**.

with the attributes:  
- `size` - size of the hash table
- `values` - a Python list spanning the size of the hash table, pre-filled with the **None** placeholder

and the following methods:  
- `repr()` - returns a formatted string containing the values in the hash table
- `_hash(key)`
    - takes in a `string` argument `key`
    - returns a hashed `integer` value denoting the `location` using a hash function. For simplicity, the _hash method has been implemented for you. `Take note, this will not be the case for exams.`
- `_rehash(old_location)`
	-  returns a new location (for linear probing)
    - <details>
		<summary>Tip</summary>
		How do I implement rehash for linear probing?
		<ul>
		<li>Simply increment the old location to move to the next slot.
		<li>If you're at the end of the table, wrap around to the beginning.</li>
		</ul>
		</details>
- `setitem(key, value)`
    - adds/updates a key-value pair (as a tuple) in the hash table
    - raises an `Exception` if the hashtable is full
    - <details>
		<summary>Tip</summary>
		<ul>
		<li>Step 1: Hash the key to find the starting index</li>
		<li>Step 2: Remember the starting index to detect when we've looped back to the beginning</li>  
		<li>Step 3: Search (repeatedly) for an empty slot or a matching key to update</li>  
			<ul>
				<li>Step 4: If the current slot is empty, insert the new key-value pair as a tuple</li>
				<li>Step 5: If the current slot has a matching key, update its value</li>
				<li>Step 6: Move to the next index using rehashing</li>
				<li>Step 7: If we’ve gone full circle, the table is full. Raise an exception!</li>  
			</ul>
		</ul>
		</details>
- `getitem(key)` - returns the following:
    - returns a value associated with the given key or
    - raise a `KeyError` if the key is not found
    - <details>
		<summary>Tip</summary>
		<ul>
		<li>Step 1: Hash the key to find the starting index</li>
		<li>Step 2: Remember the starting index to detect when we've looped back to the beginning</li>  
		<li>Step 3: Search (repeatedly) for matching key (ie. Start Probing)</li>  
			<ul>
				<li>Step 4: If the current slot is empty, the key doesn’t exist (stop search)</li>
				<li>Step 5: Check if the key matches the current slot</li>
				<li>Step 6: Move to the next index using rehashing</li>
				<li>Step 7: Check if we’ve gone full circle and key wasn't found. Raise a KeyError exception!</li>  
			</ul>
		</ul>
		</details>

### Task 1.1
Implement the `_rehash(old_location)` method such that:
- it accepts a string `old_location` as parameter
- and returns a integer value denoting the new location of an item in the hash table, for linear probing

### Task 1.2
Implement the rest of the methods for the Hash Table (with linear probing included).

### Task 1.3 (Optional)
Can you figure out what changes need to be implemented, if we want to include a `delitem` method?


**NOTE: Remember to include the docstrings for your methods**