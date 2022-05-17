"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""


class Solution:
    def reverse_linked_list(self, head):
        last = None
        curr = head
        next_ptr = curr
        while curr is not None:
            next_ptr = curr.next
            curr.next = last
            last = curr
            curr = next_ptr
        head = last
        return head

    def getDecimalValue(self, head: ListNode) -> int:
        head = self.reverse_linked_list(head)
        exp = 0
        val = 0
        curr = head
        while curr is not None:
            val += curr.val * pow(2, exp)
            exp += 1
            curr = curr.next
        return val


    def getDecimalValueOptimizedApproach(self,head):
        val = head.val
        curr = head.next
        while curr is not None:
            val = (val << 1) | curr.val
            curr = curr.next
        return val