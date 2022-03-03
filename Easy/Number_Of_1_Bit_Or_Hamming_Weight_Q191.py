"""

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.



Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.



Constraints:

    The input must be a binary string of length 32.

"""
import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(0,32):
            if ((n & mask) != 0):
                bits += 1
            mask <<= 1
            i += 1
        return bits

    # in the above approach there will be a minimum of 32 iterations, to reduce the iterations to number of 1s in the number we need to know the following:
    # n & n-1 = 0
    def hamming_weight_optimized_solution(self, n: int) -> int:
        bit_count = 0
        while n !=0:
            bit_count += 1
            n &= (n-1)
        return bit_count


    # def hamming_weight_one_line_solution(self,n: int) -> int:
    #     return bin(n).count(1)

# obj=Solution()
# print(obj.hamming_weight_one_line_solution(11))
# print(obj.hammingWeight(11))
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        # self.assertEqual(self.obj.hamming_weight_one_line_solution(1),1)
        self.assertEqual(self.obj.hammingWeight(1),1)
        self.assertEqual(self.obj.hamming_weight_optimized_solution(1),1)

    def test_case2(self):
        self.assertEqual(self.obj.hamming_weight_optimized_solution(11),3)
        self.assertEqual(self.obj.hammingWeight(11),3)
        # self.assertEqual(self.obj.hamming_weight_one_line_solution(11),3)

    def test_case3(self):
        self.assertEqual(self.obj.hammingWeight(128),1)
        self.assertEqual(self.obj.hamming_weight_optimized_solution(128),1)
        # self.assertEqual(self.obj.hamming_weight_one_line_solution(128),1)



