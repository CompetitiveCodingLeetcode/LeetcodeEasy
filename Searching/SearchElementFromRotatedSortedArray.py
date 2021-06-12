def find_pivot(input_list, low, high):
    mid = int((low + high) / 2)

    if high < low:
        return -1
    if low == high:
        return low
    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid
    if mid > low and input_list[mid - 1] > input_list[mid]:
        return mid - 1
    if input_list[low] >= input_list[mid]:
        return find_pivot(input_list, low, mid - 1)
    return find_pivot(input_list, mid+1, high)


def binary_search(input_list, low, high, key):

    while low <= high:
        mid = int((low + high) / 2)
        if input_list[mid] == key:
            return mid
        elif input_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def pivoted_binary_search(input_list, input_list_len, key):
    pivot = find_pivot(input_list, 0, input_list_len - 1)
    if pivot == -1:
        idx = binary_search(input_list, 0, input_list_len - 1, key)
        return idx

    if input_list[pivot] == key :
        return pivot
    if input_list[0] <= key:
        return binary_search(input_list, 0, pivot - 1, key)
    return binary_search(input_list, pivot + 1, input_list_len - 1, key)


print(pivoted_binary_search([2, 3, 4, 5, 1], 5, 4))
print(pivoted_binary_search([5, 6, 1, 2, 3, 4], 6, 3))
print(pivoted_binary_search([1, 2, 3, 4, 5], 5, 5))
