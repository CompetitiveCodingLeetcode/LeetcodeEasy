### What is hashing?
- It is a method of sorting and indexing data.
- the idea is to allow large amounts of data to be indexed using keys commonly created by formulas.

### Why Hashing?
- It is time efficient in case of SEARCH operation
    - Array/Python list - O(log n)
    - Tree (balanced) - O(log n)
    - Linked List - O(N)
    - Hashing - O(1)/O(n), O(n) when the number of collisions are there.
    
### Hashing Terminology

1. Hash function: a function that can be used to map data of arbitrary size to data of fixed size
2. Key: Input data by user
3. Hash value: A value that is returned by hash function. Also k/a hash, hash code or digest
4. Hash Table: it is a data structure which implements an associative array abstract data type , a structure that can map keys to values.
5. Collision: A collision occurs when two different keys to a hash function produce the same output(hash value).

### Hash functions

- Mod function
    - def mod(number, celNumber):
          return umber % cellNumber
- ASCII function
  - def modASCII(string,cellNumber):
        total = 0
        for i in string:
            total+= ord(i)
        return total % cellNumber 
    
### properties of good hash function
- it distributes hash values uniformly across hash tables
- It has to use all the input data. eg. ABCD and ABCDEF if we use only first four chars then the hash value will be identical

### Collision Resolution Techniques
- Direct Chaining
  - implements buckets as linked list
  - colliding elements are stored in linked lists

![Screenshot from 2021-07-02 18-39-56](https://user-images.githubusercontent.com/41982971/124286313-702ed380-db6c-11eb-8925-0437e9c8f2de.png)

- Open Addressing
  - Linear Probing
  - Quadratic Probing
  - Double Hashing
  




      