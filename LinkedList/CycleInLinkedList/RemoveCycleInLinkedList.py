from LinkedListCycleII_Q142 import Solution

def remove_cycle(head):
    obj = Solution()
    start_of_loop = obj.detectCycle(head)
    temp = start_of_loop
    while temp.next != start_of_loop:
        temp = temp.next

    temp.next = None

