### link for how dictionary is mapped in memory
https://thoughtworks.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/19179352#overview

### Major Functions used to orate with dictionaries
1. clear all elements of a dictionary
 <dict_variable>.clear()
   
2. shallow copy of dictionary : does not modify the original dictionary, a new 
dictionary is created which is filled with copy of references of the old dictionary
    <dict_variable>.copy()

3. fromkeys() method returns a new dictionary
    SYNTAX: <dict_var or {}>.fromkeys(sequence[],value)
   where sequence is the sequence of keys we want and value is optional
   value represents the value to be assigned to each key.
   If we don't specify a value  then by default it is None.
   
4. get() method is used to fetch the value of the given key in a dictionary if key is there in dictionary.
    SYNTAX: <dict_variable>.get(key,value)
    key is the key to be fetched in the dictionary
   value is optional parameter -- it is the value to be returned if the key is not present in the dictionary
   by default value=None

5. keys() method returns the list of all keys in a dictionary
   SYNTAX: <dict_variable>.keys()
   
6. values() method returns a list of all values from a dictionary
    SYNTAX: <dict_variable>.values()
   
7. items() method returns a list of key value tuple pairs
   SYNTAX: <dict_variable>.items()
   Example: myDict={'a':1,'b':2,'c':3}
   myDict.items() OUTPUT: dict_items([('a',1),('b',2),('c',3)])

8. popitem() method returns and removes an arbitrary element(key,value pair) from a dictionary.

9. pop() method deletes the key specified and returns the key value pair deleted.
    SYNTAX: <dict_variable>.pop(key,default_value)
   
10. setdefault() method returns the value of key if key is in the dictioanry.
   if not it inserts the key into the dictionary
   SYNTAX: <dict_variable>.setdefault(key,default_value)
   where key = the key to be serached in the dictioary
         default_value = the value of the key if key not found in the dictionary. By default dafault_value =  None
    
11. update() method updates the given dictionary with the elements from another dictioanry object or from an iterable
    of key value pairs.
    updates if key is in the dictionary and adds if key is not in the dictionary.
    SYNTAX: <dict_variable>.update(other_dictionary)
    
### Dictionary operations
1. in operator: returns boolean value telling if an item exists or not in the collection(here dictionary)
    here it tells if a key exists in a dictionary.
   for checking values we need to use values() method dict_variable.values()
   
**in operator uses different algorithms for list and dictionaries:
for list: Linear search hence O(n) time complexity
for dictionary: hash table hence O(1) time complexity**

2. all() : 

3. any() :

4. sorted(iterable,reverse,key) : 


### Dictionary vs List:

| LIST             | Dictionary                           |
|---------------------------------------------------------|

### Time and Space Complexity in python dictionary

1. Creating A dictionary

- Time Complexity: O(len(dict))

because for each insertion the hash table calculates hash value

- Space Complexity: O(n)


2. Inserting a value in dictionary

- Time Complexity: O(1)/O(n)

O(1) to handle the insertion in the beginning

O(n) to handle further insertions

- Space Complexity: O(1)

3. Traversing a given dictionary

- Time Complexity: O(n)

- Space Complexity: O(1)

4. Accessing a given cell

- Time Complexity: O(1)

- Space Complexity: O(1)

5. Searching a given value

- Time Complexity: O(n)
with in operator it is O(1) time complexity

- Space Complexity: O(1)

6. Deleting a given value

- Time Complexity: O(n)

- Space Complexity: O(1)
