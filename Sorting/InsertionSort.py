import unittest

def insertion_sort(input_list):
    input_list_len = len(input_list)
    for i in range(1, input_list_len):
        k = i
        temp = input_list[i]
        while k > 0 and temp < input_list[k - 1]:
            input_list[k] = input_list[k - 1]
            k -= 1
        input_list[k] = temp
    return input_list


print(insertion_sort([4, 8, 6, 3, 7]))

