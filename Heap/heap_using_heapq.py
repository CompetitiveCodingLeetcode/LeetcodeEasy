"""
by default, heapq has min heap. to operate as max heap in heapq, multiply by -1 while input and output.
"""

from heapq import heappush, heappop, heapify

#create empty heap
max_heap = []
heapify(max_heap)

#add items to heap using heappush
heappush(max_heap,-1*10)
heappush(max_heap,-1*30)
heappush(max_heap,-1*20)
heappush(max_heap,-1*400)

# print value of max element
print("max: ",str(-1*max_heap[0]))

#print heap elements
print("elements in heap:")
for i in max_heap:
    print((-1*i),end=" ")
print("\n")

element = heappop(max_heap)

print("popped element:",(-1*element))

print("max_element:",str((-1*max_heap[0])))

print("elements in heap:")
for i in max_heap:
    print((-1*i),end=" ")
print("\n")

# min heap implementation
#create empty heap
min_heap = []
heapify(min_heap)

#add items to heap using heappush
heappush(min_heap,100)
heappush(min_heap,30)
heappush(min_heap,20)
heappush(min_heap,400)

# print value of max element
print("min: ",str(min_heap[0]))

#print heap elements
print("elements in heap:")
for i in min_heap:
    print(i,end=" ")
print("\n")

element = heappop(min_heap)

print("popped element:",element)

print("min_element:",str(min_heap[0]))

print("elements in heap:")
for i in min_heap:
    print(i,end=" ")
print("\n")

