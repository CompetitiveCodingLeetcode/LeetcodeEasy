"""
Design a data structure to implement ‘N’ stacks using a single array of size ‘S’. It should support the following operations:
push(X, M): Pushes an element X into the Mth stack. Returns true if the element is pushed into the stack, otherwise false.

pop(M): Pops the top element from Mth Stack. Returns -1 if the stack is empty, otherwise, returns the popped element.
Two types of queries denote these operations :
Type 1: for push(X, M) operation.
Type 2: for pop(M) operation.
Input Format :
The first line of input contains three space-separated integers ‘N’, ‘S’ and ‘Q’ denoting the number of stacks, the size of the array and number of queries, respectively.

The next ‘Q’ lines specify the type of operation/query to be performed on the data structure.

Each query contains an integer ‘P’ denoting the type of query.

For query of type 1, the integer ‘P’ is equal to 1 and it is followed by two space-separated integers ‘X’ and ‘M’ denoting the element and stack on which operation is to be performed, respectively.

For query of type 2, the integer ‘P’ is equal to 2 and it is followed by a single integer ‘M’ denoting the stack on which operation is to be performed.
Output Format :
For each query, print the output returned after performing the corresponding operation on the data structure.
Note :
You do not need to print anything, it has already been taken care of. Just implement the given functions.
Constraints :
1 <= N <= S <= 1000
1 <= Q <= 10^5
1 <= P <= 2
1 <= X <= 10^5

Time Limit: 1 sec

Where ‘S’ represents the size of the array, ‘N’ represents the number of stacks, ‘Q’ represents the number of queries, ‘P’ represents the type of operation and ‘X’ represents the element.


Approach1:
let's say we have an array of length n. We have to implement k stacks in an array of length n. We divide array into K parts of size n/k each.
Disadvantage: It's not space optimized.


Approach2:
Let's suppose we have an array of size n(=9).
_ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8
we have to implement k(=3) stacks.

If we revisit 2 stacks in an array question, there we had 2 tops, one for each stack. we'll follow a similar approach here.

there are 2 additions here:
1)top[] : array to store top element index of each stack. size of top[] = number of stacks(here k)
Initially, the array values will be initialized to -1
2) next[] : size is equal to array size
    i) points to next element after stack top. --> this case happens when arr[i] stores an element in it
    ii) points to next free space/block ---> this happens when arr[i] is empty
Initially, since arr is empty, hence:
next[0] = 1 because next free space after arr[0] is arr[1]
next[1] = 2 because next free space after arr[1] is arr[2]
next[2] = 3 because next free space after arr[2] is arr[3]
next[3] = 4 because next free space after arr[3] is arr[4]
...
next[8] = because there's no free space after arr[8]

3) freespot: to keep track of which index in next[] array should be taken. (to keep track of next free space)
Initially, freespot = 0

PUSH operation (x,m) --> push element x in m-th stack:
1) find index of freespot
index = freespot
2) update value of freespot
freespot = next[index]
3) push element x:
arr[index]=x
4) update next[index] as one element is pushed in arr.
next[index] = top[m-1]
5) update top of m-th stack
top[m-1] = index
Time complexity: O(1)
Space complexity: O(max_size+num_of_stacks+max_size) = O(max_size+num_of_stacks)


POP operation (m) --> pop element from mth stack:
reverse the steps followed for push operation
Time complexity: O(1)
Space complexity: O(max_size+num_of_stacks+max_size) = O(max_size+num_of_stacks)
"""

class NStacks():
    def __init__(self,max_size,num_of_stacks):
        self.max_size = max_size
        self.num_of_stacks = num_of_stacks
        self.arr = [None]*self.max_size
        self.top = [-1]*self.num_of_stacks
        self.next=[]
        for i in range(1,self.max_size):
            self.next.append(i)
        self.next.append(-1)
        self.freespot = 0

    def is_full(self):
        if self.freespot == -1:
            return True
        return False

    def push(self,x,m):
        if not self.is_full():
            # update index
            index = self.freespot
            #update freespot
            self.freespot = self.next[index]
            #push the element
            self.arr[index]=x
            # update next
            self.next[index] = self.top[m-1]
            # update top
            self.top[m-1] = index
        else:
            return "Stack Full"

    def is_empty(self,m):
        if self.top[m-1] == -1:
            return True
        return False

    def pop(self,m):
        if self.is_empty(m):
            return "Stack empty"
        else:
            index = self.top[m-1]
            self.top[m-1] = self.next[index]
            self.next[index] = self.freespot
            self.freespot = index
            return self.arr[index]

obj = NStacks(5,3)
obj.push(2,1)
obj.push(3,1)
obj.push(4,1)
obj.push(12,2)
obj.push(13,2)
print(obj.push(233,3))
print(obj.pop(1))
print(obj.pop(3))