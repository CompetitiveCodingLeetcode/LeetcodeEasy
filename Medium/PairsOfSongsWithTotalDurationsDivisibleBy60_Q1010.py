"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""
import collections
import unittest
from typing import List


class Solution:
    # Time limit exceeded, time complexity: O(n^2)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num_of_pairs = 0
        time_set = set(time)
        if len(time_set) == 1:
            if time[0] % 60 == 0:
                num_of_pairs = int((len(time) * (len(time) - 1)) / 2)
                return num_of_pairs
            else:
                return num_of_pairs

        for i in range(0, len(time)):
            for j in range(i + 1, len(time)):
                total_time = time[i] + time[j]
                if total_time % 60 == 0:
                    num_of_pairs += 1

        return num_of_pairs

    # time complexity O(n)
    def numPairsDivisibleBy60_approach2(self, time: List[int]) -> int:
        """
        Intuition

        Let's dive deep into the condition (time[i] + time[j]) % 60 == 0 to examine the relation between time[i] and time[j]. Assuming that a and b are two elements in the input array time, we have:

        (a+b)% 60=0
        ((a % 60)+(b % 60))% 60=0
        Therefore, either
         a % 60 = 0
                    , (a%60)+(b%60)=60
         b % 60 = 0
        You can learn more about the modulo operation here.

        Hence, all we need would be finding the pairs of elements in time so they meet these conditions.

        Algorithm

        We would iterate through the input array time and for each element a, we want to know the number of elements b such that:

        b %60=0, if a % 60=0
        b % 60= 60 - a % 60, if a%60 != 0
        We can use Approach 1 to implement this logic by repeatedly examining the rest of time again and again for each element a. However, we are able to improve the time complexity by consuming more space - we can store the frequencies of the remainder a % 60, so that we can find the number of the complements in O(1) time.
        """
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:  # check if a%60==0 && b%60==0
                ret += remainders[0]
            else:  # check if a%60+b%60==60
                ret += remainders[60 - t % 60]
            remainders[t % 60] += 1  # remember to update the remainders
        return ret



class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.numPairsDivisibleBy60([30,20,150,100,40]),3)

    def test_case2(self):
        self.assertEqual(self.obj.numPairsDivisibleBy60([60,60,60]),3)


    def test_case1_approach2(self):
        self.assertEqual(self.obj.numPairsDivisibleBy60_approach2([30,20,150,100,40]),3)

    def test_case2_approach2(self):
        self.assertEqual(self.obj.numPairsDivisibleBy60_approach2([60,60,60]),3)