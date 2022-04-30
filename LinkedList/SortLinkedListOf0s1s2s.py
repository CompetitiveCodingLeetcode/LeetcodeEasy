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

def insert_at_tail(tail,node):
    tail.next = node
    tail = node
    return tail

def sort_approach2(head):
    #cretae three linked list for zer,1,and 2 respectively with dummy nodes in beginnning with val = -1
    zerohead = Node(-1)
    zerotail = zerohead
    onehead = Node(-1)
    onetail = onehead
    twohead = Node(-1)
    twotail = twohead

    #curr poinnting to head
    curr = head

    # make separate linked lists for zer,one and two
    while curr is not None:
        if curr.val == 0:
            zerotail = insert_at_tail(zerotail,curr)
        elif curr.val == 1:
            onetail = insert_at_tail(onetail,curr)
        else:
            twotail = insert_at_tail(twotail,curr)
        curr = curr.next

    # merge the three linked lists
    #check if onehesad is empty then onetail should point to twohead.next
    if onehead.next is None:
        zerotail.next = twohead.next
    else:
        zerotail.next = onehead.next


    onetail.next  = twohead.next
    twotail.next = None

    #head pointing to merged lists
    head = zerohead.next

    # delete the dummy heads
    del(zerohead)
    del(onehead)
    del(twohead)

    return head




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
head = sort_approach2(head)
# print(custom_ll)
temp = head
while temp is not None:
    print(temp.val, end=",")
    temp = temp.next