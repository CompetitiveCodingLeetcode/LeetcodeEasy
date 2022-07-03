"""
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem.

Examples:

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2

Explanation: The person with ID 2 does not
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.

APPROACH:

"""


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
import unittest
from typing import List


class Solution:
    def __init__(self,arr:List[List[int]]):
        self.arr = arr

    def knows(self,a,b):
        if self.arr[a][b] == 1:
            return True
        else:
            return False

    def findCelebrity(self, n: int) -> int:
        members = []

        # 1. put all the members in stack
        for i in range(0, n):
            members.append(i)
        # 2. iterate over first two elements of stack until size is more than one
        while len(members) > 1:
            curr_len = len(members)
            a = members.pop()
            b = members.pop()

            # 2.1 if a knows b then a canot be a celebrity as the celebrity knows no one in the party. Hence discard a and push back b
            if self.knows(a, b):
                members.append(b)

            if self.knows(b, a):
                members.append(a)

        # 3. now there is onl one candidate left in the stack- he might be a potential candidate for celebrity

        # 3.1 first check the row must contain all zeros - as the celebrity doesn't knnow anyone
        if len(members) == 0:
            return -1
        candidate = members.pop()
        count_zeros = 0

        for i in range(0, n):
            if not self.knows(candidate, i):
                count_zeros += 1

        # 3.2 check the column, all the elemnts in col except diagonal should be 1
        count_ones = 0

        for i in range(0, n):
            if self.knows(i, candidate):
                count_ones += 1

        if count_zeros == n and count_ones == n - 1:
            return candidate
        return -1


class TestSolution(unittest.TestCase):

    def test_case1(self):
        self.obj = Solution([[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0] ])
        self.assertEqual(self.obj.findCelebrity(4),2)

    def test_case2(self):
        self.obj = Solution([[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0]])
        self.assertEqual(self.obj.findCelebrity(4),-1)