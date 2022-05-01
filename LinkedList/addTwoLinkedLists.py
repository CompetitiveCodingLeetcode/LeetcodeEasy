"""

"""


class Solution:
    def reverse_linked_list(self, head):

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverse_linked_list(l1)
        head2 = self.reverse_linked_list(l2)
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

        while carry !=0:
            carry = digit_sum//10
            val = digit_sum%10
            temp = ListNode(val,None)
            curr.next = temp
            curr = temp



        res = self.reverse_linked_list(res)

        return res