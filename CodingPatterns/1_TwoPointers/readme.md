- to efficiently traverse or manipulate sequential data structures, such as arrays or linked lists.
- it involves maintaining two pointers that traverse the data structure in a coordinated manner, typically starting from different positions or moving in opposite directions
- Examples:
  - Reversing An Array
  - Pair with given sum in a sorted array: Given a sorted array of integers, find a pair in the array that sums to a number T.
    - Initialize two pointers at the start and end of the array namely p1 and p2.
    - we calculate the sum by adding numbers at the two indices:
    - if sum is greater than the expected sum then decrement the end pointer else increment the start pointer.
    - Repeat till you get the target sum.

### Does your problem match this pattern?
- Yes, if all of these conditions are fulfilled:
  - Linear data structure: The input data can be traversed in a linear fashion, such as an array, linked list, or string.
  - Process pairs: Process data elements at two different positions simultaneously.
  - Dynamic pointer movement: Both pointers move independently of each other according to certain conditions or criteria. In addition, both pointers might move along the same or two different data structures.

### Real-world problems
- Memory management:
  - The two pointers pattern is vital in memory allocation and deallocation
  - The memory pool is initialized with two pointers: the start pointer, pointing to the beginning of the available memory block, and the end pointer, indicating the end of the block.
  - When a process or data structure requests memory allocation, the start pointer is moved forward, designating a new memory block for allocation.
  - Conversely, when memory is released (deallocated), the start pointer is shifted backward, marking the deallocated memory as available for future allocations.


