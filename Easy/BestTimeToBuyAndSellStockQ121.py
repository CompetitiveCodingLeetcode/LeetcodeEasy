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
    #O(n^2) approach  --- TLE will come as per constraints
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


    # O(n) approach
    """
    Approach 2: One Pass
Algorithm

Say the given array is:

[7, 1, 5, 3, 6, 4]

If we plot the numbers of the given array on a graph, we get:

Profit Graph

The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley.
 We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
 
 
 NOTE: What we are actually doing is this: for every element, we are calculating the difference between that element and the minimum of all the values before that element and we are updating the maximum profit if the difference thus found is greater than the current maximum profit.
    """
    def maxProfit_approach2(self, prices: List[int]) -> int:
        min_price = max(prices)
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
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

    def test_case1_approach2(self):
        self.assertEqual(self.obj.maxProfit_approach1([7,1,5,3,6,4]),5)

    def test_case2_approach2(self):
        self.assertEqual(self.obj.maxProfit_approach1([7,6,4,3,1]),0)

    def test_case3_approach2(self):
        self.assertEqual(self.obj.maxProfit_approach1([2,4,1]),2)