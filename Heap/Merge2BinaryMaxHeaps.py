"""
Given two binary max heaps as arrays, merge the given heaps to form a new max heap.



Example 1:

Input  :
n = 4 m = 3
a[] = {10, 5, 6, 2},
b[] = {12, 7, 9}
Output :
{12, 10, 9, 7,5,6,2}
Explanation :








Your Task:
You don't need to read input or print anything. Your task is to complete the function mergeHeaps() which takes the array a[], b[], its size n and m, as inputs and return the merged max heap. Since there can be multiple solutions, therefore, to check for the correctness of your solution, your answer will be checked by the driver code and will return 1 if it is correct, else it returns 0.



Expected Time Complexity: O(n.Logn)
Expected Auxiliary Space: O(n + m)



Constraints:
1 <= n, m <= 105
1 <= a[i], b[i] <= 2*105


"""


class Solution():
    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def heapify_max_heap(self, i, a, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right

        if largest != i:
            self.swap(a, i, largest)
            self.heapify_max_heap(largest, a, n)

    def mergeHeaps(self, a, b, n, m):
        # your code here
        temp = []
        for i in range(0, m):
            temp.append(b[i])
        for i in range(0, n):
            temp.append(a[i])
        lim = (m + n) // 2
        for i in range(lim, -1, -1):
            self.heapify_max_heap(i, temp, n + m)

        return temp

sol1 = Solution()
print(sol1.mergeHeaps([10,5,6,2],[12,7,9],4,3))