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

#TODO: try doing in O(1) space complexity : https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/1345590/Python-O(n)O(1)-timememory-a-bit-explained


customLL = LinkedList()
customLL.generate_list(12, 0, 99)
print(customLL)
set_values_for_linked_list(customLL, 3)
print(customLL)