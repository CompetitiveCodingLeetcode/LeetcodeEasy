### Dynamic Programming
- There are 2 approaches in DP:
  - Top-Down Approach: Recursion + Memoization
  - Bottom-Up Approach: Tabulation method

- We try to solve a problem by DP when we are trying to find optimal solution to a bigger problem by using the optimal solution of its sub problems
- there should be overlapping sub problems to solve a problem using DP
- store the value of sub problems is k/a memoization


- First make a solution with recursion
- for memoization, store the result of the recursive call in a variable.
  - After the base case check if the ans for the sub problem is already stored or not. If stored return the result else go for recursive call.
- in case of tabulation method:
  - store the base cases results in array.
  - find the range of recursive calls and create for loop
  - convert recursive relation and create an expression for dp[i]
  - return dp[n] after the loop exits