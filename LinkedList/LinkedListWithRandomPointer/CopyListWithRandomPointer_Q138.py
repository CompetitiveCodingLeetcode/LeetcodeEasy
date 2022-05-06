"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.data = int(x)
        self.next = next
        self.random = random

def traverse(head):
    if head is None:
        print('null')
        return

        # print current node data and random pointer data
    print(head.data, end='')
    print(f'({head.random.data})' if head.random else '(X)', end=' —> ')

    # recur for the next node
    traverse(head.next)


class Solution:
    # time complexity: O(n), space complexity: O(n)
    def copyRandomList(self, head: Node) -> Node:
        original_to_new = {}
        clone_ll_head = None
        temp = head
        curr = None
        # copy the linked list with next ppointers only and also fill the original_to_new dict
        while temp is not None:
            ptr = Node(temp.data, None, None)
            if clone_ll_head is None:
                clone_ll_head = ptr
                curr = ptr
            else:
                curr.next = ptr
                curr = ptr
            temp = temp.next

        # create mapping of original and clone linked list
        temp = head
        clone_node = clone_ll_head
        while temp is not None:
            original_to_new[temp] = clone_node
            temp = temp.next
            clone_node = clone_node.next


        curr = clone_ll_head
        temp = head

        # traverse the original linked list and put random pointers
        while temp is not None:
            if temp.random is None:
                curr.random = None
            else:
                curr.random = original_to_new[temp.random]
            temp = temp.next
            curr = curr.next

        return clone_ll_head

    # time complexity: O(n), space complexity: O(1)
    def copy_random_list_optimized(self,head:Node)-> Node:
        temp = head
        clone_ll_head = None
        curr = None
        # 1. create clone linked list with next pointers
        while temp is not None:
            ptr = Node(temp.data, None, None)
            if clone_ll_head is None:
                clone_ll_head = ptr
                curr = ptr
            else:
                curr.next = ptr
                curr = ptr
            temp = temp.next

        t1 = head
        p1 = clone_ll_head
        # 2. add clone ll nodes in between original ll nodes
        while t1 is not None and p1 is not None:
            next_node = t1.next
            t1.next = p1
            t1 = next_node

            next_node = p1.next
            p1.next = t1
            p1 = next_node

        # 3. add random pointers for clone ll
        temp = head
        while temp is not None:
            if temp.next is not None:
                if temp.random is not None:
                    temp.next.random = temp.random.next
            temp = temp.next.next

        # 4. revert step 2
        t1 = head
        p1 = clone_ll_head
        while t1 is not None and p1 is not None:
            t1.next = p1.next
            t1 = t1.next

            if t1 is not None:
                p1.next = t1.next
            p1 = p1.next

        return clone_ll_head


if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.random = head.next.next.next
    head.next.next.random = head.next

    print('Original Linked List:')
    traverse(head)

    clone = Solution().copyRandomList(head)

    print('\nCloned Linked List:')
    traverse(clone)

    clone2 = Solution().copy_random_list_optimized(head)
    print("Optimized clone linked list-")
    traverse(clone2)
