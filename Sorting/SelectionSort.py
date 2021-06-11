def selection_sort(input_list):
    input_list_len = len(input_list)
    for i in range(input_list_len - 1):
        for j in range(i + 1, input_list_len):
            if input_list[j] < input_list[i]:
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp

    return input_list


print(selection_sort([8, 7, 6, 5, 4]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([2, 3, 4, 1]))
print(selection_sort([3, 2, 1, 4, 1]))
