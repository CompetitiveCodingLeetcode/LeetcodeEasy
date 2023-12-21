"""
Algo:
given: a random array.
i) build heap using heapify
ii) heap sort
    1. Swap the first and last elements of current heap
    2. reduce the size of current heap by 1
    3. heapify the smaller heap according to the property(max heap or min heap).
    We are saying that the end part of the heap is sorted after every iteration. Iterations will continue till size of heap is gretaer than 1.
"""
# time complexity: O(nlogn)
from heap import Heap

hp = Heap([None,54,53,55,52,50])

for i in range(hp.heap_size//2,0,-1):
    hp.heapify_max_heap(hp.heap_size,i)

print("heap after heapify:",hp.heap_arr[1:])
i=1
t = hp.heap_size
while t>1:
    hp.swap(i,t-1)
    t -= 1
    hp.heapify_max_heap(t,1)

print("sorted :",hp.heap_arr[1:])
