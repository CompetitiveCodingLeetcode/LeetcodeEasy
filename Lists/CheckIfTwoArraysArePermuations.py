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


def check_valid_permutation(list1,list2) -> bool:
    list1_len, list2_len = len(list1), len(list2)

    if list1_len != list2_len:
        return False
    else:
        for i in range(list1_len):
            if list1[i] not in list2:
                return False
        return True

class TestSolution(unittest.TestCase):
    def test_check_number_list(self):
        self.assertTrue(check_valid_permutation([1,2,3],[1,3,2]))

    def test_check_string_list(self):
        self.assertTrue(check_valid_permutation(['a','c','b'],['a','b','c']))

    def test_check_string_list_fail(self):
        self.assertFalse(check_valid_permutation(['a','c','b'],['a','a','a']))

    def test_check_number_list_fail(self):
        self.assertFalse(check_valid_permutation([1,2,3],[1,2,3,4]))
