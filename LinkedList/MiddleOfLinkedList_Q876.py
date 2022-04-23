from LinkedList import LinkedList,Node

class Solution():
    def middle_of_linked_list(self):
        custom_ll = LinkedList()
        custom_ll.generate_list(2,1,100)
        if custom_ll.head is None:
            return None
        slow_ptr = custom_ll.head
        fast_ptr = custom_ll.head.next
        # if custom_ll_len%2 ==0:
        #     while fast_ptr is not None:
        #         fast_ptr = fast_ptr.next.next
        #         slow_ptr = slow_ptr.next
        # else:
        #     while fast_ptr.next is not None:
        #         fast_ptr = fast_ptr.next.next
        #         slow_ptr = slow_ptr.next
        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        return slow_ptr

obj = Solution()
print(obj.middle_of_linked_list())
