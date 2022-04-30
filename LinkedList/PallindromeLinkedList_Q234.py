"""
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""

from LinkedList import LinkedList,Node
from ReverseOfLinkedList import reverse_linked_list_optimized
from MiddleOfLinkedList_Q876 import Solution1

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        list_vals = ""
        while head is not None:
            list_vals += str(head.val)
            head = head.next
        rev_list_vals = ""
        for letter in list_vals:
            rev_list_vals = letter + rev_list_vals
        if list_vals == rev_list_vals:
            return True
        else:
            return False

    def is_pallindrome_optimized_approach(self,head):
        middle = Solution1().middle_of_linked_list_with_head(head)

        middle.next = reverse_linked_list_optimized(middle.next)

        middle = middle.next
        temp = head
        while middle is not None:
            if temp.val != middle.val:
                return False
            else:
                temp = temp.next
                middle = middle.next

        return True





obj = Solution()
custom_ll = LinkedList()
node = Node(1)
custom_ll.add(node)
node = Node(0)
custom_ll.add(node)
node = Node(2)
custom_ll.add(node)
node = Node(1)
custom_ll.add(node)
node = Node(2)
custom_ll.add(node)
node = Node(0)
custom_ll.add(node)
node = Node(1)
custom_ll.add(node)
head = custom_ll.head
print(obj.is_pallindrome_optimized_approach(head))


custom_ll2 = LinkedList()
node = Node(1)
custom_ll2.add(node)
node = Node(0)
custom_ll2.add(node)
node = Node(2)
custom_ll2.add(node)
node = Node(2)
custom_ll2.add(node)
node = Node(0)
custom_ll2.add(node)
node = Node(1)
custom_ll2.add(node)
head = custom_ll2.head
print(obj.is_pallindrome_optimized_approach(head))
