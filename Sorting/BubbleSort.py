import unittest


def bubble_sort(input_list):
    input_list_len = len(input_list)
    for i in range(input_list_len):
        for j in range(input_list_len - i - 1):
            if input_list[j + 1] < input_list[j]:
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
    return input_list


# print(bubble_sort([3, 2, 6, 5, 1]), end=" ")

class TestSolution(unittest.TestCase):
    def test_worst_case(self):
        self.assertListEqual(bubble_sort([8, 7, 6, 5, 4]), [4, 5, 6, 7, 8])

    def test_average_case(self):
        self.assertListEqual(bubble_sort([1, 2, 3, 6, 5, 4]), [1, 2, 3, 4, 5, 6])

    def test_best_case(self):
        self.assertListEqual(bubble_sort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
