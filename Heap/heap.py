## TODO: implementation of heap using heapq module: done in heap_using_hepq.py file

class Heap:
    def __init__(self,arr):
        self.heap_arr = arr
        self.heap_size = len(self.heap_arr)


    def print_heap(self):
        for i in range(1,len(self.heap_arr)):
            print(self.heap_arr[i],end=",")
        print("\n")

    def swap(self,parent_idx,idx):
        temp = self.heap_arr[parent_idx]
        self.heap_arr[parent_idx] = self.heap_arr[idx]
        self.heap_arr[idx] = temp

    # Time complexity: O(logn), Space complexity:O(1)
    def insert_in_max_heap(self,val):
        """
        Algo:
        1. insert at the end of heap array
        2. now check the parent node if the current val is greater than parent then swap the vals.keep doing this step until the correct pos is found.
        """
        self.heap_size += 1
        self.heap_arr.append(val)
        if self.heap_size == 2:
            return
        idx = self.heap_size-1
        parent_idx = idx // 2

        while parent_idx > 0:
            if self.heap_arr[parent_idx] < self.heap_arr[idx]:
                self.swap(parent_idx,idx)
                idx = parent_idx
                parent_idx = idx//2
            else:
                return

    # Time complexity: O(logn), Space complexity:O(1)
    def insert_in_min_heap(self,val):

        self.heap_size += 1
        self.heap_arr.append(val)
        if self.heap_size == 2:
            return
        idx = self.heap_size -1
        parent_idx = idx//2

        while parent_idx > 0:
            if self.heap_arr[parent_idx] > self.heap_arr[idx]:
                self.swap(parent_idx,idx)
                idx = parent_idx
                parent_idx = idx//2
            else:
                return

    # time complexity: O(log n)
    def delete_from_max_heap(self):
        """
        Algo:
        1. put last element as root
        2. delete last element
        3. place the element at root at correct place(heapify):
            a. if : compare root with left child if does not satisfy max heap property, then swap. continue till current idx < size of heap.
            b. elif: compare root with right child if does not satisfy max heap property, then swap. continue till current idx < size of heap.
            c. else return
        """
        if self.heap_size == 1:
            print("nothing to delete")
        self.heap_arr[1] = self.heap_arr[self.heap_size-1]
        self.heap_arr.pop()
        self.heap_size -= 1

        for i in range(self.heap_size//2,0,-1):
            self.heapify_max_heap(self.heap_size,i)

        # idx = 1
        # while idx<self.heap_size:
        #     left_idx = 2*idx
        #     right_idx = 2*idx + 1
        #     if left_idx < self.heap_size and self.heap_arr[left_idx] > self.heap_arr[idx]:
        #         self.swap(left_idx,idx)
        #         idx = left_idx
        #     elif right_idx < self.heap_size and self.heap_arr[right_idx] > self.heap_arr[idx]:
        #         self.swap(right_idx,idx)
        #         idx = right_idx
        #     else:
        #         return
    # time complexity: O(log n)
    def delete_from_min_heap(self):
        if self.heap_size == 1:
            print("nothing to delete")

        self.heap_arr[1] = self.heap_arr[self.heap_size-1]
        self.heap_arr.pop()
        self.heap_size -= 1

        # idx = 1
        # while idx < self.heap_size:
        #     left_idx = 2*idx
        #     right_idx = 2*idx + 1
        #     if left_idx < self.heap_size and self.heap_arr[left_idx] < self.heap_arr[idx]:
        #         self.swap(left_idx,idx)
        #         idx = left_idx
        #     elif right_idx < self.heap_size and self.heap_arr[right_idx] < self.heap_arr[idx]:
        #         self.swap(right_idx,idx)
        #         idx = right_idx
        #     else:
        #         return

        for i in range((self.heap_size//2),0,-1):
            self.heapify_min_heap(self.heap_size,i)

    def heapify_max_heap(self,n,i):
        largest = i
        left = 2*i
        right = (2*i)+1

        if left < n and self.heap_arr[left] > self.heap_arr[largest]:
            largest = left
        if right < n and self.heap_arr[right] > self.heap_arr[largest]:
            largest = right

        if largest != i:
            self.swap(i,largest)
            self.heapify_max_heap(n,largest)
    def heapify_min_heap(self,n,i):
        smallest = i
        left = 2 * i
        right = (2 * i) + 1

        if left < n and self.heap_arr[left] < self.heap_arr[smallest]:
            smallest = left
        if right < n and self.heap_arr[right] < self.heap_arr[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i,smallest)
            self.heapify_min_heap(n, smallest)




heap1 = Heap([None])
heap1.insert_in_max_heap(20)
heap1.insert_in_max_heap(22)
heap1.insert_in_max_heap(10)
heap1.insert_in_max_heap(15)
heap1.insert_in_max_heap(30)
heap1.insert_in_max_heap(35)
heap1.print_heap()
min_heap = Heap([None])
min_heap.insert_in_min_heap(20)
min_heap.insert_in_min_heap(22)
min_heap.insert_in_min_heap(10)
min_heap.insert_in_min_heap(15)
min_heap.insert_in_min_heap(30)
min_heap.insert_in_min_heap(35)
min_heap.print_heap()
heap1.delete_from_max_heap()
heap1.print_heap()
min_heap.delete_from_min_heap()
min_heap.print_heap()

arr = [None,54,53,55,52,50]
heap3 = Heap(arr)
for i in range((len(heap3.heap_arr)//2),0,-1):
    heap3.heapify_max_heap(len(heap3.heap_arr),i)
heap3.print_heap()

for i in range((len(heap3.heap_arr)//2),0,-1):
    heap3.heapify_min_heap(len(heap3.heap_arr),i)
heap3.print_heap()