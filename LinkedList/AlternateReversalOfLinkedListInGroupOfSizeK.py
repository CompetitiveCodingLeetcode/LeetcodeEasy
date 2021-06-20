"""
Alternate reversal of linked list in a group of size k.
Like the first group should be reversed, the second group should be the same, the third should be reversed, the fourth should be the same, etc.
Example :

Input : 1->2->3->4->5->6->7->8,  k=2
Output : 2->1->3->4->6->5->7->8

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
        if i % 2 == 0:
            group_val_list.reverse()
            input_LL_map[i] = group_val_list
        else:
            input_LL_map[i] = group_val_list
        count = 0
    return input_LL_map


def set_values_for_linked_list(input_LL, k):
    temp = input_LL.head
    input_LL_map = traverse_and_store(input_LL, k)
    count = 0
    for i in range(int(len(input_LL) / k)):
        while count != k:
            temp.val = input_LL_map[i][count]
            temp = temp.next
            count += 1
        count = 0

#TODO: write other approach using stack

customLL = LinkedList()
customLL.generate_list(12, 0, 99)
print(customLL)
set_values_for_linked_list(customLL, 3)
print(customLL)
