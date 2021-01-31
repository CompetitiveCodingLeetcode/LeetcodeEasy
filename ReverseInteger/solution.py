
"""Given a signed
32 - bit
integer
x,
return x
with its digits reversed.If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.

Assume
the
environment
does
not allow
you
to
store
64 - bit
integers(signed or unsigned).

Example
1:

Input: x = 123
Output: 321

Example
2:

Input: x = -123
Output: -321

Example
3:

Input: x = 120
Output: 21

Example
4:

Input: x = 0
Output: 0

Constraints:

-231 <= x <= 231 - 1"""

class Solution:
    def reverse(self, x: int) -> int:
        num = x
        rev = 0
        flag = 0
        while num != 0 :
            if num < 0:
                num = -1*num
                flag = 1
            d = num%10
            num = int(num/10)
            rev = rev*10+d
        if rev < -2**31 or rev > 2**31-1:
             return 0
        else:
            if flag == 1:
                return -1*rev
            else:
                return rev

num = -123
obj=Solution()
print(obj.reverse(int(num)))