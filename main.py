from hashtable_open_addressing import HashTable
import csv

if __name__ == "__main__":
    ht = HashTable(30)
    """
    1. Extract the records from the student_data file
    and add them one at a time, as a Python dict, 
    containing the name, class and their associated
    data as key-value dict pairs, to the hashtable
    
    2. You can use the id as the hash table key for 
    each of the above records.
    """
    ids = []
    with open('student_data.csv', 'r') as f:
      reader = csv.DictReader(f)
      
      for row in reader:
        id = row['id']
        ids.append(id)
        ht.setitem(id, row)
        
      # f.close() runs automatically
    
    for id in ids:
      print(ht.getitem(id))
    
    ht.delitem('s0002b')
    print('---- Expected: KeyError raised since s0002b is deleted. -----')
    print(ht.getitem('s0002b'))
    
    # Test your hashtable using appropriate methods
    # from your implementation