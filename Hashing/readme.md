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

- Open Addressing : colliding elements are stored in other vacant buckets. During storage and lookup these are found through so called probing.
  - Linear Probing: It places new key into closest following empty cell.
  - Quadratic Probing: adding arbitrary quadratic polynomial to the index until an empty cell is found
  
  ![Screenshot from 2021-07-10 08-29-57](https://github.com/CompetitiveCodingLeetcode/LeetcodeEasy/blob/main/Hashing/images/Screenshot%20from%202021-07-10%2008-29-57.png)
  
  - Double Hashing: interval between probes is calculated by another hashing function
    
    ![Screenshot from 2021-07-10 08-33-36](https://github.com/CompetitiveCodingLeetcode/LeetcodeEasy/blob/main/Hashing/images/Screenshot%20from%202021-07-10%2008-33-36.png)
  

### Hash Table is Full

- Direct chaining : this case will not arise
- Open Addressing: create a hash table of 2X size and re calculate hash values for all the keys
   - this is time consuming because the hash function is called again for all the keys hence if n keys then O(n) time complexity.
    
### Pros and Cons of Collision techniques:

![Screenshot from 2021-07-10 08-59-34](https://github.com/CompetitiveCodingLeetcode/LeetcodeEasy/blob/main/Hashing/images/Screenshot%20from%202021-07-10%2008-59-34.png)

![](https://github.com/CompetitiveCodingLeetcode/LeetcodeEasy/blob/main/Hashing/images/Screenshot%20from%202021-07-10%2009-00-50.png)


### Practical Use Of Hashing

1. Passwords on servers:
    - when we input or passwords there are 2 cases either we store the passwords as it s or we pass the passwords through a hash function and store the hash value of the password. In the first case the hackers can easily get the passwords by hacking the servers.
2. File system:
    -  File path is mapped to physical location on disk using hash functions.

### Pros and Cons of hashing
- on an average insertion/deletion/search operations take O(1) time complexity (using good hash function)
![](
- when hash function is not good enough then insertion/deletion/search operations take O(n) time complexity
![](

      
