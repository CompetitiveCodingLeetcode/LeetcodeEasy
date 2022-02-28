"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


Constraints:

1 <= n <= 104
"""
import unittest
from typing import List


class Solution:
    # time complexity: O(n); Space complexity: O(1)
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3 ==0:
                ans.append("Fizz")
            elif i%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


    # time complexity: O(n); space complexity: O(1)
    def fizzbuzz_neater_approach(self,n: int) -> List[str]:
        """

        This approach won't reduce the asymptotic complexity, but proves to be a neater solution when FizzBuzz comes with a twist. What if FizzBuzz is now FizzBuzzJazz i.e.

3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
If you try to solve this with the previous approach the program would have too many conditions to check:

Divisible by 3
Divisible by 5
Divisible by 7
Divisible by 3 and 5
Divisible by 3 and 7
Divisible by 7 and 3
Divisible by 3 and 5 and 7
Not divisible by 3 or 5 or 7.
This way if the FizzBuzz mappings increase, the conditions would grow exponentially in your program.

Algorithm

Instead of checking for every combination of these conditions, check for divisibility by given numbers i.e. 3, 5 as given in the problem. If the number is divisible, concatenate the corresponding string mapping Fizz or Buzz to the current answer string.

For eg. If we are checking for the number 15, the steps would be:

Condition 1: 15 % 3 == 0 , num_ans_str = "Fizz"
Condition 2: 15 % 5 == 0 , num_ans_str += "Buzz"
=> num_ans_str = "FizzBuzz"
So for FizzBuzz we just check for two conditions instead of three conditions as in the first approach.

Similarly, for FizzBuzzJazz now we would just have three conditions to check for divisibility.
        """
        ans = []
        ans_str = ""
        for i in range(1,n+1):
            if i%3 == 0:
                ans_str += "Fizz"
            if i%5 == 0:
                ans_str += "Buzz"
            if not ans_str:
                ans_str = str(i)
            ans.append(ans_str)
            ans_str = ""
        return ans

    # time complexity: O(n); space complexity: O(1)
    def fizzbuzz_optimized_approach(self,n: int) -> List[str]:
        """
        Intuition

This approach is an optimization over approach 2. When the number of mappings are limited, approach 2 looks good. But what if you face a tricky interviewer and he decides to add too many mappings?

Having a condition for every mapping is not feasible or may be we can say the code might get ugly and tough to maintain.

What if tomorrow we have to change a mapping or may be delete a mapping? Are we going to change the code every time we have a modification in the mappings?

We don't have to. We can put all these mappings in a Hash Table.

Algorithm

Put all the mappings in a hash table. The hash table fizzBuzzHash would look something like { 3: 'Fizz', 5: 'Buzz' }
Iterate on the numbers from 1 ... N1...N.
For every number, iterate over the fizzBuzzHash keys and check for divisibility.
If the number is divisible by the key, concatenate the corresponding hash value to the answer string for current number. We do this for every entry in the hash table.
Add the answer string to the answer list.
This way you can add/delete mappings to/from to the hash table and not worry about changing the code.

So, for FizzBuzzJazz the hash table would look something like { 3: 'Fizz', 5: 'Buzz', 7: 'Jazz' }
        """

        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n + 1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.fizzBuzz(3),["1","2","Fizz"])

    def test_case2(self):
        self.assertListEqual(self.obj.fizzBuzz(5),["1","2","Fizz","4","Buzz"])

    def test_case3(self):
        self.assertListEqual(self.obj.fizzBuzz(15),["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

    def test_case1_approach2(self):
        self.assertListEqual(self.obj.fizzbuzz_neater_approach(3),["1","2","Fizz"])

    def test_case2_approach2(self):
        self.assertListEqual(self.obj.fizzbuzz_neater_approach(5),["1","2","Fizz","4","Buzz"])

    def test_case3_approach2(self):
        self.assertListEqual(self.obj.fizzbuzz_neater_approach(15),["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

    def test_case1_optimized_approach(self):
        self.assertListEqual(self.obj.fizzbuzz_optimized_approach(3),["1","2","Fizz"])

    def test_case2_optimized_approach(self):
        self.assertListEqual(self.obj.fizzbuzz_optimized_approach(5),["1","2","Fizz","4","Buzz"])

    def test_case3_optimized_approach(self):
        self.assertListEqual(self.obj.fizzbuzz_optimized_approach(15),["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])