"""
check if the two lists are permutations of each other

example:
list1=['a','b','c']
list2=['a','c','b']
output: true
list1 and list2 are permutations of each other.

list1=[1,2,3]
list2=[2,1,3]
output: true

list1=[1,2,3]
list2=[1,4,3]
output: false

"""
import unittest


# this approach fails for test_check_string_list_with_duplicates_fail()
def check_valid_permutation(list1, list2) -> bool:
    list1_len, list2_len = len(list1), len(list2)

    if list1_len != list2_len:
        return False
    else:
        for i in range(list1_len):
            if list1[i] not in list2:
                return False
        return True


def check_valid_permutation_optimized(list1, list2) -> bool:
    list1_len, list2_len = len(list1), len(list2)
    elements_map = {}

    if list1_len != list2_len:
        return False
    else:
        for i in range(0, list1_len):
            if list1[i] in elements_map:
                elements_map[list1[i]] += 1
            else:
                elements_map[list1[i]] = 1
            if list2[i] in elements_map:
                elements_map[list2[i]] -= 1
            else:
                elements_map[list2[i]] = -1
        for val in elements_map.values():
            if val != 0:
                return False
    return True


class TestSolution(unittest.TestCase):
    def test_check_number_list(self):
        self.assertTrue(check_valid_permutation([1, 2, 3], [1, 3, 2]))

    def test_check_string_list(self):
        self.assertTrue(check_valid_permutation(['a', 'c', 'b'], ['a', 'b', 'c']))

    def test_check_string_list_fail(self):
        self.assertFalse(check_valid_permutation(['a', 'c', 'b'], ['a', 'a', 'a']))

    def test_check_number_list_fail(self):
        self.assertFalse(check_valid_permutation([1, 2, 3], [1, 2, 3, 4]))

    def test_check_string_list_with_duplicates_fail(self):
        self.assertFalse(check_valid_permutation(['a', 'c', 'b', 'a', 'd', 'b'], ['a', 'c', 'c', 'b', 'd', 'd']))

    def test_check_number_list2(self):
        self.assertTrue(check_valid_permutation_optimized([1, 2, 3], [1, 3, 2]))

    def test_check_string_list2(self):
        self.assertTrue(check_valid_permutation_optimized(['a', 'c', 'b'], ['a', 'b', 'c']))

    def test_check_string_list_fail2(self):
        self.assertFalse(check_valid_permutation_optimized(['a', 'c', 'b'], ['a', 'a', 'a']))

    def test_check_number_list_fail2(self):
        self.assertFalse(check_valid_permutation_optimized([1, 2, 3], [1, 2, 3, 4]))

    def test_check_string_list_with_duplicates_fail2(self):
        self.assertFalse(
            check_valid_permutation_optimized(['a', 'c', 'b', 'a', 'd', 'b'], ['a', 'c', 'c', 'b', 'd', 'd']))
