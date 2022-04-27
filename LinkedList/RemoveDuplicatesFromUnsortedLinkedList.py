"""
suppose there's a linked list
1->2->2->3->3->3->4->None

the o/p should be: 1->2->3->4->None
"""

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        visited_nodes = {}
        if head is None or head.next is None:
            return head
        else:
            curr = head
            prev = None
            fwd = curr.next
            while curr is not None:
                if curr.val in visited_nodes.keys():
                    prev.next = fwd
                    del(curr)
                    curr = fwd
                else:
                    visited_nodes[curr.val] = True
                    prev = curr
                    curr = fwd
                if fwd is not None:
                    fwd = curr.next
            return head