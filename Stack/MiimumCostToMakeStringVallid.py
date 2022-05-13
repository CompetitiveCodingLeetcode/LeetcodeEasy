"""
Problem Statement
Ninja has been given a string ‘STR’ containing either ‘{’ or ‘}’. 'STR’ is called valid if all the brackets are balanced. Formally for each opening bracket, there must be a closing bracket right to it.
For Example:
“{}{}”, “{{}}”, “{{}{}}” are valid strings while “}{}”, “{}}{{}”, “{{}}}{“ are not valid strings.
Ninja wants to make ‘STR’ valid by performing some operations on it. In one operation, he can convert ‘{’ into ‘}’ or vice versa, and the cost of one such operation is 1.
Your task is to help Ninja determine the minimum cost to make ‘STR’ valid.
For Example:
Minimum operations to make ‘STR’ =  “{{“ valid is 1.
In one operation, we can convert ‘{’ at index ‘1’ (0-based indexing) to ‘}’. The ‘STR’ now becomes "{}" which is a valid string.

Note:
Return -1 if it is impossible to make ‘STR’ valid.
Input Format :
The first line contains an integer 'T' which denotes the number of test cases or queries to be run. Then the test cases follow.

The only line of each test case contains a string 'STR'.
Output Format :
For each test case, print the minimum cost needed to make ‘STR’ valid.

Print -1 if it is impossible to make ‘STR’ valid.

Print the output of each test case in a separate line.
Note :
You are not required to print the expected output, it has already been taken care of. Just implement the function.
Constraints :
1 <= T <= 100
0 <= |STR| <= 10^5
STR[i] = ‘{’ or ‘}’

Time Limit: 1 sec
Sample Input 1:
2
{{{}
{{}{}}
Sample Output 1:
1
0
Explanation For Sample Input 1:
For the first test case:
The two valid strings that can be obtained from  ‘STR’ using minimum operations “{{}}”   and “{}{}”. Ninja can transform ‘STR’ to “{{}}” by performing the following operations:
Convert ‘{’ at index 2 to ‘}’.

Ninja can transform ‘STR’ to “{}{}” by performing the following operations:
Convert ‘{‘ at index 1 to ‘}’.
The minimum number of operations in transforming ‘STR’ to either of the two valid strings is 1.So, the total cost is 1.

For the second test case:
Given ‘STR’ is already valid so the minimum number of
operations required is 0.
So, the total cost is 0.
Sample Input 2:
3
{}}{}}
{{{{
{{{}}
Sample Output 2:
1
2
-1
"""
import unittest


def findMinimumCost(str):
    # Write your code here.
    if len(str) % 2 != 0:
        return -1
    else:
        opening_braces = 0
        closing_braces = 0
        stack = []
        for ch in str:
            if ch == '{':
                stack.append(ch)
                opening_braces += 1
            else:
                if len(stack) != 0:
                    stack.pop()
                    opening_braces -= 1
                else:
                    closing_braces += 1

        # 		print("opening=",opening_braces)
        # 		print("closing=",closing_braces)

        return ((opening_braces + 1) // 2) + ((closing_braces + 1) // 2)

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(findMinimumCost("{{{}"),1)

    def test_case2(self):
        self.assertEqual(findMinimumCost("{{}{}}"),0)

    def test_case3(self):
        self.assertEqual(findMinimumCost("{}}{}}"),1)

    def test_case4(self):
        self.assertEqual(findMinimumCost("{{{{"),2)

    def test_case5(self):
        self.assertEqual(findMinimumCost("{{{}}"),-1)