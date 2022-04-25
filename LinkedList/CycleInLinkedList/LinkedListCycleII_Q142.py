"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?


APPROACH:
1. detect if there is cycle in the linked list (cycle exists if slowptr = fastptr)
2. as soon as slowptr = fastptr put slowptr = head
3. now increment bith slowptr and fastptr by 1 and the point where slowptr=fastptr is the starting of cycle.

How did the aboive derivatio came into existence?
let A be distance from start of linked list to start of loop
Let B be distance from start of loop to the point where loop in cycle is detected at step 1 of approach
let c be distance of cycle / loop

distance by fastptr = 2*(distannce by slowptr)
A + x*(C) + B = 2*(A+y*(C) +B); where x= number of cycles covered by fastptr and y = number of cycles covered by slowptr
A+Cx+B = 2A +2Cy+2B
(x-2y)C = A+B
let x-2y = k
A+B = kC

the above eqn tells that A+B means cycle is completed
that means if fastptr is at B distance then it would require A dist to complete the cycle.

"""


class Solution:
    #time complexity: O(n) and space complexity: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow_ptr = head
        fast_ptr = head
        has_cycle = False

        while slow_ptr is not None and fast_ptr is not None:
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                break
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            if slow_ptr == fast_ptr:
                has_cycle = True
                slow_ptr = head
                break

        if has_cycle:
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return slow_ptr
        else:
            return None