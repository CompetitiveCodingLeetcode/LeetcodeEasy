"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?


Two pointer approach: from educative

Two pointers, left and right, are set at the head node. Move the right pointer n steps forward. After doing that, both pointers are exactly separated by n nodes apart. Start moving both pointers forward until the right pointer reaches the last node. At this point, the left pointer will be pointing to the node before the target node, i.e., the
nth last node. We relink the left node to the node following the left’s next node.

If the right pointer reaches NULL while moving it n steps forward, it means that the head node should be removed. We return the head's next node.

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        temp = n
        while temp != 0:
            right = right.next
            temp -= 1
        if right is None:
            head = head.next
            left.next = None
            return head
        while right.next is not None:
            left = left.next
            right = right.next
        temp = left.next
        left.next = temp.next
        temp.next = None
        return head


