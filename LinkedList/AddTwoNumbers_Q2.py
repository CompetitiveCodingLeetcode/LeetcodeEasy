"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Example 4:
l1=[2,4,9]
l2=[5,6,4,9]
o/p: [7,0,4,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class Solution:
    def reverse_linked_list(self, head):
        last = None
        current = head
        while current is not None:
            next_ptr = current.next
            current.next = last
            last = current
            current = next_ptr
        head = last
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        res = None
        carry = 0
        val = 0
        digit_sum = 0
        while head1 is not None and head2 is not None:
            digit_sum = carry + head1.val + head2.val
            carry = digit_sum // 10
            val = digit_sum % 10
            temp = ListNode(val, None)
            if res is None:
                res = temp
                curr = temp
            else:
                curr.next = temp
                curr = temp
            head1 = head1.next
            head2 = head2.next

        while head1 is not None:
            digit_sum = carry + head1.val
            carry = digit_sum // 10
            val = digit_sum % 10
            temp = ListNode(val, None)
            if res is None:
                res = temp
                curr = temp
            else:
                curr.next = temp
                curr = temp
            head1 = head1.next

        while head2 is not None:
            digit_sum = carry + head2.val
            carry = digit_sum // 10
            val = digit_sum % 10
            temp = ListNode(val, None)
            if res is None:
                res = temp
                curr = temp
            else:
                curr.next = temp
                curr = temp
            head2 = head2.next

        if carry > 0:
            temp = ListNode(carry, None)
            curr.next = temp
            curr = temp

        return res
