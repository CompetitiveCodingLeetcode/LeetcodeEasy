"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.



Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.
Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.


Constraints:

n == satisfaction.length
1 <= n <= 500
-1000 <= satisfaction[i] <= 1000
"""



from typing import List

class Solution:
    def solve(self, satisfaction, index, time):
        if index >= len(satisfaction):
            return 0
        include = (time + 1) * satisfaction[index] + self.solve(satisfaction, index + 1, time + 1)
        exclude = self.solve(satisfaction, index + 1, time)

        return max(include, exclude)

    def solveMem(self, satisfaction, index, time, ans_store):
        if index >= len(satisfaction):
            return 0
        if ans_store[index][time] != -1:
            return ans_store[index][time]
        include = (time + 1) * satisfaction[index] + self.solveMem(satisfaction, index + 1, time + 1, ans_store)
        exclude = self.solveMem(satisfaction, index + 1, time, ans_store)

        ans_store[index][time] = max(include, exclude)
        return ans_store[index][time]

    def solveTab(self, satisfaction):
        n = len(satisfaction)
        ans_store = []
        for i in range(0, n + 1):
            temp = []
            for j in range(0, n + 1):
                temp.append(0)
            ans_store.append(temp)
        for index in range(n - 1, -1, -1):
            for time in range(index, -1, -1):
                include = (time + 1) * satisfaction[index] + ans_store[index + 1][time + 1]
                exclude = ans_store[index + 1][time]
                ans_store[index][time] = max(include, exclude)
        return ans_store[0][0]

    def solveTabSO(self, satisfaction):
        n = len(satisfaction)
        curr = []
        nxt = []
        for i in range(0, n + 1):
            curr.append(0)
            nxt.append(0)
        for index in range(n - 1, -1, -1):
            for time in range(index, -1, -1):
                include = (time + 1) * satisfaction[index] + nxt[time + 1]
                exclude = nxt[time]
                curr[time] = max(include, exclude)
            nxt = curr
        return nxt[0]

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        index = 0
        time = 0
        satisfaction = sorted(satisfaction)
        # ans = self.solve(satisfaction,index,time)
        # n = len(satisfaction)
        # ans_store = []
        # for i in range(0,n+1):
        #     temp = []
        #     for j in range(0,n+1):
        #         temp.append(-1)
        #     ans_store.append(temp)
        # ans = self.solveMem(satisfaction,index,time,ans_store)

        # ans = self.solveTab(satisfaction)

        # doesn't work
        ans = self.solveTabSO(satisfaction)

        return ans
