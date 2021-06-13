"""
Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln. Rearrange the nodes in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 …
You are required to do this in place without altering the nodes’ values.

Examples:

Input:  1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3

Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3

"""

from LinkedList import LinkedList


def arrange_linked_list(input_ll):
    input_ll_len = len(input_ll)
    if input_ll_len > 1:
        if input_ll_len % 2 == 0:
            mid_count = int(input_ll_len / 2)
        else:
            mid_count = int(input_ll_len / 2) + 1
        prev = None
        last = None
        curr = input_ll.head
        next_ptr = input_ll.head

        while mid_count != 0:
            prev = curr
            curr = curr.next
            next_ptr = next_ptr.next
            mid_count -= 1

        prev.next = None
        new_LL = LinkedList()
        new_LL.head = curr

        while curr is not None:
            next_ptr = curr.next
            curr.next = last
            last = curr
            curr = next_ptr
        new_LL.head = last

        curr_temp = input_ll.head
        next_temp = curr_temp
        new_curr_temp = new_LL.head
        new_next_temp = new_curr_temp

        while new_curr_temp is not None and curr_temp is not None:
            next_temp = curr_temp.next
            new_next_temp = new_curr_temp.next
            curr_temp.next = new_curr_temp
            new_LL.head = new_next_temp
            new_curr_temp.next = next_temp
            new_curr_temp = new_next_temp
            curr_temp = next_temp
        new_LL.head = None


customLL = LinkedList()
customLL.generate_list(15, 0, 99)
print(customLL)
arrange_linked_list(customLL)
print(customLL)
