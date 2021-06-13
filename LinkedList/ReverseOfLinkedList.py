"""
Reverse a linked list
i/p-- 1 -> 2 -> 3 -> 4 -> 5
o/p -- 5 -> 4 -> 3 -> 2 -> 1

"""

from LinkedList import LinkedList


def reverse_linked_list(input_ll):
    stack_ll = []
    sptr = input_ll.head
    fptr = input_ll.head
    while sptr is not None:
        stack_ll.append(sptr.val)
        sptr = sptr.next

    while fptr is not None:
        fptr.val = stack_ll.pop()
        fptr = fptr.next


customLL = LinkedList()
customLL.generate_list(12, 0, 99)
print(customLL)
reverse_linked_list(customLL)
print(customLL)