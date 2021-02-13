"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.


"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            smallest_word_len = len(strs[0])
            ps = 0
            for pos, str in enumerate(strs):
                new_len = len(str)
                if smallest_word_len > new_len:
                    smallest_word_len = new_len
                    ps = pos
            output = ""
            compare = strs[pos - 1]
            for i in range(0, smallest_word_len):
                for str in strs:
                    if compare[i] != str[i]:
                        return output
                output += str[i]
            return output
        else:
            return ""

obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flip"]))