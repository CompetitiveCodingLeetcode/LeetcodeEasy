"""
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 106
"""



"""
Approach followed:
1. it follows Seive of Eratosthenes principle
2. Assume the current number to be prime starting from 2 and set state of multiples of that number to be false for isPrime().
3. go to next number.
4. if true then increment the count else keep moving until next number with state true is reached or n is reached.

The time complexity of the following is : O(n(log(logn)))
expolanation:

for 2: 
n/2 elements are visited.
for 3 :
n/3 elements are visited.
for 5:
n/5 and so on

hence series looks like:
((n/2)+(n/3)+(n/5).....)
(n*(1/2+1/3+1/5+....))
the inner series is H.P. of prime numbers.
Using taylor series:
(1/2+1/3+1/5...)=log(log n)
Hence,
(n*(1/2+1/3+1/5+....)) = n*(log(log n))

"""
import unittest


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        nums = [True] * (n + 1)
        nums[0] = False
        if n > 1:
            nums[1] = False

        for i in range(2, n):
            if nums[i]:
                count += 1
                j = 2 * i
                while j < n:
                    nums[j] = False
                    j += i

        return count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.countPrimes(10),4)

    def test_case2(self):
        self.assertEqual(self.obj.countPrimes(0),0)

    def test_case3(self):
        self.assertEqual(self.obj.countPrimes(1),0)

