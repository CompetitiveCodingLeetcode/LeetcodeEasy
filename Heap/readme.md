## what is heap?

- it is a data structure.
- it is a complete binary tree that comes with a heap order property.
  - binary tree: every node can have atmost 2 children
  - complete binary tree: every level is completely filled except the last level. Nodes always added from the left.
  - Heap Order Property: there are 2 types of properties: min heap property, max heap property. Min heap property means the child nodes will be greater than its parent node. Max heap property means the child nodes will be less than the parent node.

## insertion in heap:
- if we store a heap in an array then following properties hold true:
  - Assumption: the root is counted as idx 1 and array idx starts with 1 instead of 0.
  1. if node is at ith idx in array then left child is at 2*i idx and right child is at 2*i+1.
  2. if a node is at ith idx then its parent lies at int(i/2) idx in array.
  - Assumption: the root is counted as idx 0 and array idx starts with 0.
  1. if node is at ith idx in array then left child is at (2*i)+1 idx and right child is at 2*i+2.
  2. if a node is at ith idx then its parent lies at int(i/2) idx in array.

## deletion in heap:
- in case of heap deletion means delete the root.

## heapify algorithm:
- In a complete binary tree:
  - leaf nodes lie from ((n/2)+1)th index to nth index.
  - leaf node can be assumed to be a heap in itself.
  - from (n/2)th index to 0, do heapify to convert into max or min heap.
    - Algo:
      - assign i as largest and find the left node idx and right node idx.
      - check condition for left and right nodes and update values of largest
      - if value of largest has been chnages then it would not be equal to i and hence swap the elements at largest and i and call heapify for rest of the elements.

## heap sort

## priority queue as min or max heap
- to avoid writing code for min and max heap we can use priority queue data structure.
- we should use heapq module to use priority queue as heap
- https://docs.python.org/3/library/heapq.html
- https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

## custom heap using heapq:
- https://www.geeksforgeeks.org/heapq-with-custom-predicate-in-python/
- check for max heap situation

## Applications of Heap:
- find kth largest element in an array
  - Algo 1:
    - sort the array in descending order
    - return element at k-1 th position in the array.
    - Time complexity: O(nlogn)
  - Algo 2 using heap:
    - 