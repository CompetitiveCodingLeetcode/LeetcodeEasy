### QUEUE
- it is a data structure that stores items in **FIFO** manner.


### opeartions in Queue
- Creating Queues
- Enqueue()
- Dequeue()
- peek(), delete(), isEmpty(), isFull()
- delete queue

### Implementation in Queue
1. Python List
    - Queue without capacity
    - Queue with capacity(Circular Queue)
    
2. Linked List

### Time and Space complexity for Queue
1. Create Queue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
2. Enqueue
   - Time Complexity - O(n)
   - Space Complexity - O(1)
3. Dequeue
   - Time Complexity - O(n)
   - Space Complexity - O(1)
4. Peek
   - Time Complexity - O(1)
   - Space Complexity - O(1)
5. isEmpty
   - Time Complexity - O(1)
   - Space Complexity - O(1)
6. Delete Entire Queue
   - Time Complexity - O(1)
   - Space Complexity - O(1)   

### Time and Space complexity for Queue with capacity
1. Create Queue
   - Time Complexity - O(1)
   - Space Complexity - O(n) because all the n elements are filled as None. 
2. Enqueue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
3. Dequeue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
4. Peek
   - Time Complexity - O(1)
   - Space Complexity - O(1)
5. isEmpty
   - Time Complexity - O(1)
   - Space Complexity - O(1)
6. Delete Entire Queue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
7. isFull
   - Time Complexity - O(1)
   - Space Complexity - O(1)

### Time and Space complexity for Queue Linked List
1. Create Queue
   - Time Complexity - O(1)
   - Space Complexity - O(1) 
2. Enqueue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
3. Dequeue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
4. Peek
   - Time Complexity - O(1)
   - Space Complexity - O(1)
5. isEmpty
   - Time Complexity - O(1)
   - Space Complexity - O(1)
6. Delete Entire Queue
   - Time Complexity - O(1)
   - Space Complexity - O(1)
   
## Queue using Python Modules
- There are 3 modules that can be used to create queues:
   - Collections module
   - python queue module
   - multiprocessing module
   
1. Collections Module
- It supports adding and removing of elements in O(1) time complexity
- The collections.deque class:
   - deque() - create or initialize the queue with or without capacity
   - append() - add elements to the end of the queue 
   - popleft() - remove first element from the queue
   - clear() - delete all elements from the queue

2. Queue module
- It is useful in threaded programming where information must be safely exchanged between multiple threads
- This module implements three type of queue:
   - FIFO
   - LIFO(Stack)
   - Priority Queue
- FIFO:
    - Methods used:
        - Queue(maxsize=0) - if maxsize is 0 then the size of the queue will be infinite and if a number is specified then that will be the size of the queue
        - qsize() - returns the size of the queue
        - empty() - returns True if the queue is empty else false
        - full() - returns true if the size of queue is reached
        - put() - append element at the end of the queue
        - get() - remove element from the start of the queue
        - task_done() - not understood
        - join() - not understood

3. multiprocessing module
- allows two items to be processed in parallel by multiple concurrent workers
- multiprocessing queue is meant for sharing data between processes and can store nay packable objects.
- It uses same methods as Queue module
   
