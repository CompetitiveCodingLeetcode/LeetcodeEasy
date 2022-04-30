"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

#time complexity: O(n), space complexity: O(1)
class Solution:
    def solve(self, list1, list2):
        prev = list1
        curr = list1.next

        temp2 = list2

        while curr is not None and temp2 is not None:

            if prev.val <= temp2.val < curr.val:
                prev.next = temp2
                prev = temp2
                temp2 = temp2.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        if temp2 is not None:
            prev.next = temp2

        return list1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            return self.solve(list1, list2)
        else:
            return self.solve(list2, list1)