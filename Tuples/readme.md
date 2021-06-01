### What are tuples?

Tuples are **immutable** sequence of objects.

They are comparable and hashable.

### How to create a tuple?

- to create a tuple create comma separated values

Example: myTuple='a','b','c' or myTuple=('a','b','c')

For creating tuple with only one element keep the comma entact at the end
myTuple = ('a',)


- **Time Complexity Of Creating a Tuple** O(1)

- **Space Complexity Of Creating a Tuple** O(n)


### Tuples in Memory / Accessing Tuple Elements

- elements of tuple ar located in memory contiguously
- The main difference between tuples and arrays is that tuples are immutable.
- To access elements of tuple we use [] operator or slice operator [:]

### Two ways of searching in tuple

- in operator
- linear search

index(tuple_element) returns the index of the tuple element specified.

### Tuple operations or functions

- '+' operator: concatenates two tuples and returns a tuple
- '*' operator: repeats the elements of tuples the number of times specified.
- in operator
- count(tuple_element): returns the number of times the tuple element occurs in the tuple
- index(tuple_element): returns the index of the tuple element specified
- len(tuple_variable):returns the length of the tuple
- max(tuple_variable):returns the max value in tuple
- min(tuple_variable):returns the minimum value in tuple
- tuple(list_variable): converts a **list** to **tuple**

### Tuple vs List

- *List* is **mutable** whereas *Tuple* is **immutable**.
- We can reassign the entire tuple but we cannot change the single tuple value
    Example:
  tuple1=0,9,8,7,6
  
   tuple1=5,4,3,2

    but tuple1[0]=33 gives TypeError

- deletion of entire tuple possible but deletion of one element in tuple not possible

- **We use tuples for heterogeneous data types and lists for homogeneous data types**
- Iterating through tuple is faster than list
- Tuples that contain immutable elements can be used as a key for the dictionaries
- **If you have data that doesn't change, implementing that data as tuple will guarantee that it remains write-protected**


### Time and Space Complexity on Tuples

1. Creating a Tuple
-  Time Complexity: O(1) because you can specify all elements in one go
- Space Complexity: o(n)
  
2. Traversing a given tuple
- Time Complexity: O(n)
- Space Complexity: O(1)

3. Accessing a given element
- Time Complexity: O(1)
- Space Complexity: O(1)

4. Searching a given element
- Time Complexity: O(n)
- Space Complexity: O(1)

