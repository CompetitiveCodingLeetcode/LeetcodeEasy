"""
Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.

The amount of petrol that every petrol pump has.
Distance from that petrol pump to the next petrol pump.
Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1-litre petrol, the truck can go 1 unit of distance.
For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where the truck can make a circular tour is 2nd petrol pump. Output should be “start = 1” (index of 2nd petrol pump).

"""
import unittest
from typing import List


class Solution():
    # here the time complexity is O(n) and at max each element will be visited twice,
    def find_first_circular_tour(self,arr: List[List[int]]):
        n = len(arr)
        balance = 0
        front = 0
        rear = 0
        ans = -1

        for i in range(0,n):
            balance += arr[i][0] - arr[i][1]
            if balance < 0:
                if front == n-1:
                    front = 0
                else:
                    # instead of doing front += 1, we are doing front = rear+1 because if i=0 and we cannot go beyond
                    # index 2 due to less fuel then there will be no possible paths when i=1 or i=2 because when i=0
                    # then some balance of fuel is added further and still we aren't able to go further then not
                    # possible when we freshly start at index 1 or 2.
                    front = rear + 1
                rear = front
                balance = 0
            else:
                if rear == n-1:
                    rear = 0
                else:
                    rear += 1

            if front == rear:
                ans = i+1

        return ans

    def find_first_circular_tour_one_pass(self,arr):
        n = len(arr)
        balance = 0
        deficit = 0
        start = 0

        for i in range(0,n):
            balance += arr[i][0] - arr[i][1]
            if balance < 0:
                deficit += balance
                balance = 0
                start = i+1

        if deficit+balance >= 0:
            return start
        else:
            return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.find_first_circular_tour([[6,4], [3,6], [7,3]]),2)

    def test_case2(self):
        self.assertEqual(self.obj.find_first_circular_tour_one_pass([[6,4], [3,6], [7,3]]),2)



