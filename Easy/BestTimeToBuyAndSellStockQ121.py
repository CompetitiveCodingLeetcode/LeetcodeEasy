"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
import unittest
from typing import List


class Solution:
    #O(n^2) approach
    def maxProfit_approach1(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = 0
        for idx, price in enumerate(prices):
            if idx != len(prices) - 1:
                max_price = max(prices[idx + 1:])
            if max_price > price:
                if max_price - price > max_profit:
                    max_profit = max_price - price

        return max_profit


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1_approach1(self):
        self.assertEqual(self.obj.maxProfit_approach1([7,1,5,3,6,4]),5)

    def test_case2_approach1(self):
        self.assertEqual(self.obj.maxProfit_approach1([7,6,4,3,1]),0)

    def test_case3_approach1(self):
        self.assertEqual(self.obj.maxProfit_approach1([2,4,1]),2)