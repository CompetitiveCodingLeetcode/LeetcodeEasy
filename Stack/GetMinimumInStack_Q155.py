"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.


APPROACH:
Approach1:
add minimum at each step to another stack(minstack) and as you pop the val from stack, pop value from minstack as well. Also, getmin() method returns top of minstack.

Time complexity: O(1)
Space complexity: O(n)


Approach2:
PUSH(val) :
i) first push operation:
    push val to stack
    update minimum to val
ii) a) if value_to_be_pushed < minimum:
        value_to_be_pushed = 2 *val - minimum
        minimum = val
        push temp to stack
    b) push val to stack

POP:
i) fetch top value of stack
ii) pop from stack
iii) a)if value in i) < minimum
        prev_min = minimum
        val = 2* minimum - value in i)
        popped val = prev_min
        minimum = val
    b) popped val = value in i)

TOP:
i) fetch the element in top of stack
ii) a) if value in i) < minimum
        return minimum
    b) return value in i)

getMin:
return minimum variable.

Time Complexity: O(1)
Space complexity: O(1)

"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        if self.is_empty():
            self.minimum = val
            self.stack.append(val)
        else:
            if val < self.minimum:
                temp = 2 * val - self.minimum
                self.minimum = val
                self.stack.append(temp)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.is_empty():
            print("Stack is empty")
        else:
            curr = self.stack[-1]
            self.stack.pop(-1)
            if curr < self.minimum:
                prev_minimum = self.minimum
                val = 2*self.minimum - curr
                print("popped value = ",prev_minimum)
                self.minimum = val
            else:
                print("here")
                print("popped value = ",curr)


    def top(self) -> int:
        if self.is_empty():
            return -1
        else:
            curr = self.stack[-1]
            if curr < self.minimum:
                val = self.minimum
            else:
                val = curr
            return val

    def getMin(self) -> int:
        return self.minimum

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) #return -3
minStack.pop()
print(minStack.top())    #return 0
print(minStack.getMin()) #return -2