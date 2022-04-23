"""
Reverse a linked list
i/p-- 1 -> 2 -> 3 -> 4 -> 5
o/p -- 5 -> 4 -> 3 -> 2 -> 1

"""

from LinkedList import LinkedList


#Time complexity - O(n) Space Complexity - O(n)
def reverse_linked_list_stack_approach(input_ll):
    stack_ll = []
    sptr = input_ll.head
    fptr = input_ll.head
    while sptr is not None:
        stack_ll.append(sptr.val)
        sptr = sptr.next

    while fptr is not None:
        fptr.val = stack_ll.pop()
        fptr = fptr.next

#Time complexity - O(n), space complexity-O(n)
def reverse_linked_list_recursively(head):
    if head == None or head.next == None:
        return head

    left_ll_head = reverse_linked_list_recursively(head.next)
    head.next.next = head
    head.next = None

    return left_ll_head
    


# Time Complexity - O(n) Space Complexity - O(1)
def reverse_linked_list_optimized_approach(input_ll):
    current = input_ll.head
    last = None
    next_ptr = input_ll.head
    while current is not None:
        next_ptr = current.next
        current.next = last
        last = current
        current = next_ptr
    input_ll.head = last


customLL = LinkedList()
customLL.generate_list(12, 0, 99)
print(customLL)
reverse_linked_list_stack_approach(customLL)
print(customLL)
reverse_linked_list_optimized_approach(customLL)
print(customLL)
print("recursive approach")
customLL_head = reverse_linked_list_recursively(customLL.head)
while customLL_head != None:
    print(customLL_head.val,end=",")
    customLL_head = customLL_head.next