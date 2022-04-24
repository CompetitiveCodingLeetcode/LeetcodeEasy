"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:

Input: head = [1], k = 1
Output: [1]



Constraints:

    The number of nodes in the list is in the range sz.
    1 <= sz <= 5000
    0 <= Node.val <= 1000
    1 <= k <= sz


Follow-up: Can you solve the problem in O(1) extra memory space?
"""


from LinkedList import LinkedList


def traverse_and_store(input_LL, k):
    temp = input_LL.head
    input_LL_map = {}
    count = 0

    for i in range(int(len(input_LL) / k)):
        group_val_list = []
        while count != k:
            group_val_list.append(temp.val)
            count += 1
            temp = temp.next
        # group_val_list.reverse()
        input_LL_map[i] = group_val_list
        count = 0
    return input_LL_map


def set_values_for_linked_list(input_LL, k):
    temp = input_LL.head
    input_LL_map = traverse_and_store(input_LL, k)
    count = 0
    for i in range(int(len(input_LL) / k)):
        while count != k:
            temp.val = input_LL_map[i].pop()
            temp = temp.next
            count += 1
        count = 0

# does not work in case of [1,2,3,4,5] and k=3 ans should be 3,2,1,4,5 however the ans given by my soln is 3,2,1,5,4
def recursive_approach(input_ll_head,k):
    if input_ll_head == None:
        return None

    curr = input_ll_head
    prev = None
    fwd = curr.next
    count = 0

    while curr is not None and count<k:
        fwd = curr.next
        curr.next = prev
        prev = curr
        curr = fwd

        count += 1

    if fwd is not None:
        input_ll_head.next = recursive_approach(fwd,k)

    return prev

#TODO: try doing in O(1) space complexity : https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/1345590/Python-O(n)O(1)-timememory-a-bit-explained
def optimized_approach(input_ll,k):
    head = input_ll.head
    count=1
    prev = None
    curr = head
    fwd = curr.next
    next_k = head
    while curr is not None :
        while count%3 != 0 :
            count += 1
            next_k = next_k.next

        curr.next = next_k.next
        prev = curr
        curr = fwd
        fwd = fwd.next



customLL = LinkedList()
customLL.generate_list(12, 0, 99)
print(customLL)
set_values_for_linked_list(customLL, 3)
print(customLL)
print("calling recursive approach")
head = recursive_approach(customLL.head,3)
while head is not None:
    print(head.val,end=",")
    head = head.next
# print("optimized approach")
# optimized_approach(customLL,3)
# print(customLL)
