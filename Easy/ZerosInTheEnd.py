"""

In a list push all the zeros at the end of the list and non-zero elements should be in the same order.


Approach: maintain index for non zero elements'
Instead of pushing zeros at the end push non zero elemnts in the beginning

"""


def push_non_zero_elements(input_list):
    list_len = len(input_list)
    i=0
    for num in input_list:
        if num!=0:
            input_list[i] = num
            i+=1
    for idx in range(i,list_len):
        input_list[idx]=0
    return input_list

print(push_non_zero_elements([1,0,5,6,0,4,7,0]))