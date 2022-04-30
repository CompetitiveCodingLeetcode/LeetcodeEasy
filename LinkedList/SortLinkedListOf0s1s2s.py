"""

"""
from LinkedList import LinkedList,Node


def sort_approach1(head):
    count_nums = [0]*3
    temp = head
    while temp is not None:
        if temp.val == 0:
            count_nums[0] += 1
        elif temp.val == 1:
            count_nums[1] += 1
        else:
            count_nums[2] += 1
        temp = temp.next

    temp = head
    while count_nums[0] !=0:
        temp.val = 0
        count_nums[0] -= 1
        temp = temp.next

    while count_nums[1] != 0:
        temp.val = 1
        count_nums[1] -= 1
        temp = temp.next

    while count_nums[2] != 0:
        temp.val = 2
        count_nums[2] -= 1
        temp = temp.next


custom_ll = LinkedList()
node = Node(1)
custom_ll.add(node)
node = Node(0)
custom_ll.add(node)
node = Node(2)
custom_ll.add(node)
node = Node(1)
custom_ll.add(node)
node = Node(0)
custom_ll.add(node)
node = Node(2)
custom_ll.add(node)
node = Node(1)
custom_ll.add(node)
print(custom_ll)
head = custom_ll.head
sort_approach1(head)
print(custom_ll)