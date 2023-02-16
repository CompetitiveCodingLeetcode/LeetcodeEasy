class Heap:
    def __init__(self):
        self.heap_arr = [None]
        self.heap_size = 0

    def print_heap(self):
        for i in range(1,self.heap_size+1):
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
        if self.heap_size == 1:
            return
        idx = self.heap_size
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
        if self.heap_size == 1:
            return
        idx = self.heap_size
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
        3. place the element at root at correct place:
            a. if : compare root with left child if does not satisfy max heap property, then swap. continue till current idx < size of heap.
            b. elif: compare root with right child if does not satisfy max heap property, then swap. continue till current idx < size of heap.
            c. else return
        """
        if self.heap_size == 0:
            print("nothing to delete")
        self.heap_arr[1] = self.heap_arr[self.heap_size]
        self.heap_arr.pop()
        self.heap_size -= 1

        idx = 1
        while idx<self.heap_size:
            left_idx = 2*idx
            right_idx = 2*idx + 1
            if left_idx <= self.heap_size and self.heap_arr[left_idx] > self.heap_arr[idx]:
                self.swap(left_idx,idx)
                idx = left_idx
            elif right_idx <= self.heap_size and self.heap_arr[right_idx] > self.heap_arr[idx]:
                self.swap(right_idx,idx)
                idx = right_idx
            else:
                return

    # time complexity: O(log n)
    def delete_from_min_heap(self):
        if self.heap_size == 0:
            print("nothing to delete")

        self.heap_arr[1] = self.heap_arr[self.heap_size]
        self.heap_size -= 1

        idx = 1
        while idx < self.heap_size:
            left_idx = 2*idx
            right_idx = 2*idx + 1
            if left_idx <= self.heap_size and self.heap_arr[left_idx] < self.heap_arr[idx]:
                self.swap(left_idx,idx)
                idx = left_idx
            elif right_idx <= self.heap_size and self.heap_arr[right_idx] < self.heap_arr[idx]:
                self.swap(right_idx,idx)
                idx = right_idx
            else:
                return






heap1 = Heap()
heap1.insert_in_max_heap(20)
heap1.insert_in_max_heap(22)
heap1.insert_in_max_heap(10)
heap1.insert_in_max_heap(15)
heap1.insert_in_max_heap(30)
heap1.insert_in_max_heap(35)
heap1.print_heap()
min_heap = Heap()
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
