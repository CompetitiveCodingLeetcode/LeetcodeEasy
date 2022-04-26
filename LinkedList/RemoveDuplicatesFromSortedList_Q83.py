"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            curr = head
            while curr is not None:
                if curr.next is not None and curr.val != curr.next.val:
                    curr = curr.next
                elif curr.next is not None:
                    node_to_be_deleted = curr.next
                    next_next = curr.next.next
                    del(node_to_be_deleted)
                    curr.next = next_next
                else:
                    curr = curr.next
            return head