"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.



Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.


Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.


APPROACH:

APPROACH 1 (Time Limit Exceeded):
If the ith bill amount - 5 > 0 then:
    i) find array elements that make the sum equal to bill[i]-5 using subset approach.
    ii) if an ans is obtained then remove the elements from change array. Else if ans is empty return False.
    iii) append current amount in change array.
    return true

APPROACH 2:
Let's try to simulate giving change to each customer buying lemonade. Initially, we start with no five dollar bills, and no ten dollar bills.

If a customer brings a ＄5 bill, then we take it.

If a customer brings a ＄10 bill, we must return a five dollar bill. If we don't have a five dollar bill, the answer is False, since we can't make correct change.

If a customer brings a ＄20 bill, we must return ＄15.

If we have a ＄10 and a ＄5, then we always prefer giving change in that, because it is strictly worse for making change than three ＄5 bills.

Otherwise, if we have three ＄5 bills, then we'll give that.

Otherwise, we won't be able to give ＄15 in change, and the answer is False.


"""
import unittest
from typing import List


class Solution:
    def find_sum(self, diff, change, output, index, ans):
        if index >= len(change):
            if sum(output) == diff:
                ans.append(output.copy())
            return
        else:
            # include call
            element = change[index]
            output.append(element)
            self.find_sum(diff, change, output, index + 1, ans)
            output.pop()
            # exclude call
            self.find_sum(diff, change, output, index + 1, ans)

    def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        for i in range(0, len(bills)):
            if bills[i] - 5 > 0:
                ans = []
                output = []
                index = 0
                diff = bills[i] - 5
                self.find_sum(diff, change, output, index, ans)
                if len(ans) == 0:
                    return False
                # make changes to change
                if ans:
                    for val in ans[0]:
                        change.remove(val)
            change.append(bills[i])
        return True

    def lemonadeChangeOptimized(self, bills: List[int]) -> bool:
        five=ten=0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case_1(self):
        self.assertTrue(self.obj.lemonadeChange([5,5,5,10,20]))

    def test_case_2(self):
        self.assertFalse(self.obj.lemonadeChange([5,5,10,10,20]))

    def test_case_3(self):
        self.assertTrue(self.obj.lemonadeChangeOptimized([5,5,5,10,20]))

    def test_case_4(self):
        self.assertFalse(self.obj.lemonadeChangeOptimized([5,5,10,10,20]))
