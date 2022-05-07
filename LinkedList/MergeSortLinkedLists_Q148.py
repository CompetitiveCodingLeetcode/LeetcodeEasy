"""

"""
from LinkedList import Node,LinkedList

class Solution:
    def find_middle_node(self, head):
        if head is None :
            return head
        prev = None
        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr is not None and slow_ptr is not None:
            fast_ptr = fast_ptr.next
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        return prev

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        res = Node()
        temp = res
        while left is not None and right is not None:
            if left.val < right.val:
                temp.next = left
                left = left.next
                temp = temp.next
            else:
                temp.next = right
                right = right.next
                temp = temp.next

        while left is not None:
            temp.next = left
            left = left.next
            temp = temp.next

        while right is not None:
            temp.next = right
            right = right.next
            temp = temp.next

        res = res.next
        return res

    def sortList(self, head: Node) -> Node:

        # base case
        if head is None or head.next is None:
            return head

        # find middle of linked list and break it into left and right parts
        middle = self.find_middle_node(head)

        left = head
        right = middle.next
        middle.next = None

        # recursively sort the two linked lists
        left = self.sortList(left)
        right = self.sortList(right)

        # merge the two linked lists
        res = self.merge(left, right)

        return res


custom_ll = LinkedList()
custom_ll.generate_list(12,0,99)
print("original list")
print(custom_ll)
print("sorted list")
head = Solution().sortList(custom_ll.head)
while head is not None:
    print(head.val,end=",")
    head = head.next

