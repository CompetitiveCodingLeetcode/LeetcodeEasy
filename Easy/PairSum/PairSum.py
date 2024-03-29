"""
You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.
Note:

Each pair should be sorted i.e the first value should be less than or equals to the second value.

Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

Input Format:

The first line of input contains two space-separated integers 'N' and 'S', denoting the size of the input array and the value of 'S'.

The second and last line of input contains 'N' space-separated integers, denoting the elements of the input array: ARR[i] where 0 <= i < 'N'.

Output Format:

Print 'C' lines, each line contains one pair i.e two space-separated integers, where 'C' denotes the count of pairs having sum equals to given value 'S'.

Note:

You are not required to print the output, it has already been taken care of. Just implement the function.

Constraints:

1 <= N <= 10^3
-10^5 <= ARR[i] <= 10^5
-2 * 10^5 <= S <= 2 * 10^5

Time Limit: 1 sec

Sample Input 1:

5 5
1 2 3 4 5

Sample Output 1:

1 4
2 3

Explaination For Sample Output 1:

Here, 1 + 4 = 5
      2 + 3 = 5
Hence the output will be, (1,4) , (2,3).

Sample Input 2:

5 0
2 -3 3 3 -2

Sample Output 2:

-3 3
-3 3
-2 2


"""


def sort_key(ans):
    return ans[0]


def pairSum(arr, s):
    # Write your code here.
    ans = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            temp = []
            if arr[i] + arr[j] == s:
                temp.append(min(arr[i], arr[j]))
                temp.append(max(arr[i], arr[j]))
                ans.append(temp)

    ans.sort(key=sort_key)
    return ans

print(pairSum([1, 2, 3, 4, 5], 5))
print(pairSum([2, -3, 3, 3, -2],0))