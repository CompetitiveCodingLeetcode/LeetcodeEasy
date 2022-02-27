"""
Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


Constraints:

1 <= n <= 1000
"""



"""
APPROACH:
Intuition
Naive idea
n = 1, [0]
n = 2, [-1, 1]

Now write more based on this
n = 3, [-2, 0, 2]
n = 4, [-3, -1, 1, 3]
n = 5, [-4, -2, 0, 2, 4]

It spreads like the wave.


Explanation
Find the rule
A[i] = i * 2 - n + 1


Math Observation
@zzg_zzm helps explain in math.

Actually, this rule could be derived from constructing an arithmetic sequence.

(Note that any arithmetic sequence must have unique values if the common delta is non-zero)

We need the sequence sum, so that

(a[0] + a[n-1]) * n / 2 = 0, which means a[0] + a[n-1] = 0.

Note that a[n-1] - a[0] = (n-1) * delta, which is -2 * a[0],

so we simply set delta = 2, a[0] = 1 - n


Note
It's not bad to sum up 1 + 2 + 3 + ... + (N - 1).
Personally I don't really like it much.
What is the possible problem of this approach?
It doesn't work if N goes up to 10^5


Complexity
Time O(N)
Space O(N)
"""
import unittest
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1 - n, n, 2))

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.sumZero(5),[-4,-2,0,2,4])

    def test_case2(self):
        self.assertListEqual(self.obj.sumZero(3),[-2,0,2])

    def test_case3(self):
        self.assertEqual(self.obj.sumZero(1),[0])


