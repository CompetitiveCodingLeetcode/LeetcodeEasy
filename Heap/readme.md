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
  - from 0 to (n/2)th index, do heapify to convert into max or min heap.
    - Algo:
      - assign i as largest and find the left node idx and right node idx.
      - check condition for left and right nodes and update values of largest
      - if value of largest has been chnages then it would not be equal to i and hence call heapify for rest of the elements.