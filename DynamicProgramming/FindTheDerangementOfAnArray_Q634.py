"""
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

You are given an integer n. There is originally an array consisting of n integers from 1 to n in ascending order, return the number of derangements it can generate. Since the answer may be huge, return it modulo 109 + 7.



Example 1:

Input: n = 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
Example 2:

Input: n = 2
Output: 1


Constraints:

1 <= n <= 106


APPROACH:
1. we have numbers in array from 1 to n
2. ways in which 1 can be put are n-1.
solution will be (n-1)* solution to subproblems
there are two cases in the above:
1. 1 is put at ith postition and i is put at position 1 i.e., both values are swapped. hence, wee have n-2 positions to be swapped with n-2 values. hence f(n-2) ways.
2. 1 is put at ith postition  but i is not put at position of 1. no swapping hence we have n-1 number to be placed in n-1 positions which is f(n-1) ways.

hence our recurrence relation looks like:
f(n) = (n-1)*[f(n-2)+f(n-1)]
"""

