"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8


"""
import unittest
from typing import List

# Approach 1 TLE ---> for n=6
class Solution1:
    def isValid(self, s):
        st = []
        bracket_dict = {"(": ")"}
        index = 0
        for c in s:
            if c in bracket_dict:
                st.append(c)
                index += 1
            else:
                # for the following test case : test_invalid_no_opening_symbol
                if index == 0:
                    return False
                if bracket_dict[st[index - 1]] == c:
                    index -= 1
                    st.pop(index)
                else:
                    return False
        if len(st):
            return False
        return True

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def generate_valid_permutations(self, arr, idx, ans, n, ans_map):
        if idx >= n:
            temp_str = ''.join(arr)
            if self.isValid(temp_str):
                if temp_str not in ans_map.keys():
                    ans_map[temp_str] = True
                    ans.append(temp_str)

        for i in range(idx, n):
            self.swap(arr, idx, i)
            self.generate_valid_permutations(arr, idx + 1, ans, n, ans_map)
            self.swap(arr, idx, i)

    def generateParenthesis(self, n: int) -> List[str]:
        idx = 0
        opening_bracket = '('
        closing_bracket = ')'
        arr = []

        for i in range(0, 2 * n):
            if i < n:
                arr.append(opening_bracket)
            else:
                arr.append(closing_bracket)

        ans = []
        ans_map = {}
        self.generate_valid_permutations(arr, idx, ans, 2 * n, ans_map)

        return list(set(ans))


"""
 to generate all parenthesis using recursion and kep them in a set

Approach
to form a well formed paranthesis string our initial string must be '(' then we keep count of open brack and close brackets from here and out to generate all possible string, the opem brackets (o) must not be higher than n and you can only use a close bracket (e) if and only if open bracket(o) count is strictly greater than (e) by using these 2 if conditions we need to create two recursive calls until we reach a string s of length 2*n, we add the string to s and return , this way we can generate all possible string

1. The idea is to add ')' only after valid '('
2. We use two integer variables left & right to see how many '(' & ')' are in the current string
3. If left < n then we can add '(' to the current string
4. If right < left then we can add ')' to the current string

For n = 2, the recursion tree will be something like this,

								   	(0, 0, '')
								 	    |	
									(1, 0, '(')  
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					res.append('(())')             res.append('()()')
   

 """
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj=Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.generateParenthesis(3),["((()))","(()())","(())()","()(())","()()()"])

    def test_case2(self):
        self.assertListEqual(self.obj.generateParenthesis(1),["()"])