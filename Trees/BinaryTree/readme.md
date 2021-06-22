### Questions List

- https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
- https://www.geeksforgeeks.org/sum-of-nodes-at-maximum-depth-of-a-binary-tree-set-2/

### Binary Tree
- data structures in which each node has at most two children, left and right children
- It is a family of data structure (BST, Heap tree, AVL, red black trees, Syntax tree)

### Why Binary Tree?
- prerequisite for more advanced trees like BST, AVL, Red Black Trees
- Huffman Coding Problem, Heap priority problem and expression parsing problems can be solved efficiently using binary trees

### Types of Binary Tree

- Full Binary Tree
    - If a node has zero children or two children
- Perfect Binary Tree
    - all nodes have exactly two children and leaf nodes are at same level
- Complete Binary Tree
    - last level is not completely filled
    - the nodes are as left as possible for the incomplete level
- Balanced Binary Tree
    - all leaf nodes are located from the root in the same distance
  
### Binary Tree
- Linked List
- Python List(array)

#### Linked List Representation
- each node has data, left reference and right reference.

  
    
  ![Screenshot from 2021-06-20 21-28-57](https://user-images.githubusercontent.com/41982971/122680934-738e9a80-d20f-11eb-864a-0ebb77731a31.png)

#### Python List Representation
- to make mathematical calculations easier we are assuming that we will not fill the cells at 0 location
- if x is the index of the current node:
   - left node will be at 2x index
   - right node will be at 2x+1 index
  
### Complexities for Binary Tree Operations

1. Creation pf Binary Tree
- Time Complexity: O(1)
- Space Complexity: O(1)

2. Traversals 
- Depth First search
  - Pre Order Traversal
    - Time Complexity: O(n) because O(n/2)+O(n/2)
    - Space Complexity: O(n) because we are using stack memory
  - In order Traversal
    - Time Complexity: O(n) because O(n/2)+O(n/2)
    - Space Complexity: O(n) because we are using stack memory
  - Post Order Traversal
    - Time Complexity: O(n) because O(n/2)+O(n/2)
    - Space Complexity: O(n) because we are using stack memory
- Breadth First Search
  - Level Order Traversal
    