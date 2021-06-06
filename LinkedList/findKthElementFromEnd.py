# Approach 1: for finding kth element from end means it is (n-k+1)th element from beginning
# This approach takes 2 scans each of O(n) time complexity thereby at the end resulting time complexity of O(n)

from LinkedList import LinkedList


def find_kth_element_from_end_approach1(linked_list, k):
    temp = linked_list.head
    limit = len(linked_list) - k + 1
    for i in range(1, limit):
        temp = temp.next
    return temp.val


# this approach takes O(n) time complexity but one scan
def find_kth_element_from_end_approach2(linked_list, k):
    temp = linked_list.head
    ptr1 = linked_list.head
    ptr2 = temp
    count = 1
    while ptr2.next:
        if count == k:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        else:
            count += 1
            ptr2 = ptr2.next
    return ptr1.val


customList = LinkedList()
customList.generate_list(12, 0, 99)
print(customList)
print(find_kth_element_from_end_approach1(customList, 3))
print(find_kth_element_from_end_approach2(customList, 3))
