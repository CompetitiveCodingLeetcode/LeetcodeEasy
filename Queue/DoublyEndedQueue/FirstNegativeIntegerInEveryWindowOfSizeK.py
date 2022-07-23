"""
Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.



Example 1:

Input :
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output :
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Example 2:
Input :
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0


Your Task:
You don't need to read input or print anything. Your task is to complete the function printFirstNegativeInteger() which takes the array A[], its size N and an integer K as inputs and returns the first negative number in every window of size K starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

Constraints:
1 <= N <= 105
-105 <= A[i] <= 105
1 <= K <= N
"""

from doublyEndedQueue import DoubleEndedQueue

# time complexity: O(nk)
def printFirstNegativeInteger(A, N, K):
    # code here
    ans = []
    for i in range(0, N - K + 1):
        temp = A[i:i + K]
        x = [j for j in temp if j < 0]
        if len(x) == 0:
            ans.append(0)
        else:
            ans.append(x[0])

    return ans

# time complexity: O(n), Space complexity: O(k)
def printFirstNegativeInteger_approach2(A,N,K):
    ans = []
    dq = DoubleEndedQueue(len(A))
    #process first window
    for i in range(0,K):
        if A[i] < 0:
            dq.push_back(i)

    # update ans for first window
    if not dq.is_empty():
        ans.append(A[dq.queue[dq.front]])
    else:
        ans.append(0)

    #process for rest of the windows
    for i in range(K,N):
        # remove the unwanted window answer from ans
        if not dq.is_empty() and (i-dq.queue[dq.front] >= K):
            dq.pop_front()
        # addition
        if A[i] < 0:
            dq.push_back(i)
        #update answer
        if not dq.is_empty():
            ans.append(A[dq.queue[dq.front]])
        else:
            ans.append(0)
    return ans

#TODO: optimized approach with O(1) space complexity


print(printFirstNegativeInteger([12, -1, -7, 8, -15, 30, 16, 2],8,3))
print(printFirstNegativeInteger_approach2([12, -1, -7, 8, -15, 30, 16, 2],8,3))