"""
Given two sets A and B and target is K.
Find the pair of elements one from each list that sum to k.

"""

def pair_of_elements(list1,list2,k):
    list1_len = len(list1)
    list2_len = len(list2)
    temp_map = {}

    if list1_len < list2_len:
        for i in range(list2_len):
            if list2[i] not in temp_map:
                temp_map[list2[i]] = i
        for i in range(list1_len):
            diff = k - list1[i]
            if diff in temp_map:
                return True
        return False

    else:
        for i in range(list1_len):
            if list1[i] not in temp_map:
                temp_map[list1[i]] = i
        for i in range(list2_len):
            diff = k - list2[i]
            if diff in temp_map:
                return True
        return False


print(pair_of_elements([1,2,3,4,4,7,9],[2,3,4,5,6],15))