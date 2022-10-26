"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.



Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17


Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

APPROACH:
Approach 1: Row Sum Maximum
Intuition

We know the amount of money that each customer has in each of the NN banks. The total wealth of a customer is the sum of all the money that he/she has in all the banks. As an example, the table below shows three customers, the money each of them has in the 44 banks, and their total wealth. Once we have the total wealth for each customer, we can compare them and return the highest total.

fig

The solution described above can be broken down into two steps:

Find the wealth of each customer and store it in a list.
Find and return the greatest wealth contained in the list.
We can change it to a single-step solution. Instead of storing the wealth in a list, we can keep a variable maxWealthSoFar. It will store the highest wealth we have seen so far and it will be initialized to 00 because that's the minimum wealth possible. This way we can find the highest wealth by comparing just after calculating it instead of first storing in a list.

Algorithm

Iterate over the customers i.e., accounts.
For each account in accounts, we iterate over the money deposited in different banks and add it to currCustomerWealth.
Compare currCustomerWealth with maxWealthSoFar. If currCustomerWealth is greater than maxWealthSoFar then update maxWealthSoFar.
Return maxWealthSoFar.

Complexity Analysis

Let MM be the number of customers and NN be the number of banks.

Time complexity: O(M⋅N)

For each of the MM customers, we need to iterate over all NN banks to find the sum of his/her wealth. Inside each iteration, operations like addition or finding maximum take O(1)O(1) time. Hence, the total time complexity is O(M \cdot N)O(M⋅N).

Space complexity: O(1)

We only need two variables currCustomerWealth and maxWealthSoFar to store the wealth of the current customer, and the highest wealth we have seen so far respectively. Therefore, the space complexity is constant.

"""
import unittest
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        local_sum = 0
        for account in accounts:
            local_sum = sum(account)
            if local_sum > max_wealth:
                max_wealth = local_sum

        return max_wealth

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.maximumWealth([[1,2,3],[3,2,1]]),6)

    def test_case2(self):
        self.assertEqual(self.obj.maximumWealth([[1,5],[7,3],[3,5]]),10)

    def test_case3(self):
        self.assertEqual(self.obj.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]),17)